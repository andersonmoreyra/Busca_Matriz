from django.test import TestCase
from assets.models import Ativo, CentroCusto, Local
from .models import PlanoManutencao, GatilhoManutencao, TarefaPreventiva

class MaintenancePlanningTest(TestCase):
    def setUp(self):
        self.centro_custo = CentroCusto.objects.create(codigo="CC03", descricao="Manutencao")
        self.local = Local.objects.create(nome="Local A")
        self.ativo = Ativo.objects.create(nome="Motor Elétrico", codigo_patrimonio="MOT-01", centro_custo=self.centro_custo, local=self.local)

        self.plano = PlanoManutencao.objects.create(
            titulo="Revisão Mensal Motor",
            ativo=self.ativo
        )

        self.gatilho = GatilhoManutencao.objects.create(
            plano=self.plano,
            tipo="tempo",
            valor_referencia=30,
            unidade_medida="dias"
        )

        self.tarefa = TarefaPreventiva.objects.create(
            plano=self.plano,
            descricao="Inspecionar ruídos",
            ordem_execucao=1
        )

    def test_plano_criacao(self):
        self.assertEqual(self.plano.ativo.nome, "Motor Elétrico")

    def test_gatilho_criacao(self):
        self.assertEqual(self.gatilho.tipo, "tempo")
        self.assertEqual(self.gatilho.valor_referencia, 30)

    def test_tarefa_preventiva(self):
        self.assertEqual(self.tarefa.ordem_execucao, 1)
        self.assertEqual(self.tarefa.plano.titulo, "Revisão Mensal Motor")
