from django.test import TestCase
from datetime import date
from assets.models import Ativo, Local
from orders.models import SolicitacaoManutencao, OrdemServico
from .models import ParadaProgramada, VinculoParadaOS

class ProjectsTest(TestCase):
    def setUp(self):
        self.local = Local.objects.create(nome="Linha de Envasamento")
        self.ativo = Ativo.objects.create(nome="Envasadora", codigo_patrimonio="ENV-01", local=self.local)

        self.parada = ParadaProgramada.objects.create(
            titulo="Grande Parada Anual",
            local_afetado=self.local,
            data_inicio_prevista=date(2024, 1, 10),
            data_fim_prevista=date(2024, 1, 20),
            status="planejamento"
        )

        self.solicitacao = SolicitacaoManutencao.objects.create(ativo=self.ativo, descricao="Falha")
        self.os = OrdemServico.objects.create(numero="OS-P-01", ativo=self.ativo, solicitacao_origem=self.solicitacao, descricao="Troca de correias")

        self.vinculo = VinculoParadaOS.objects.create(
            parada=self.parada,
            ordem_servico=self.os
        )

    def test_parada_programada(self):
        self.assertEqual(self.parada.titulo, "Grande Parada Anual")
        self.assertEqual(self.parada.status, "planejamento")

    def test_vinculo_os(self):
        self.assertEqual(self.vinculo.parada.titulo, "Grande Parada Anual")
        self.assertEqual(self.vinculo.ordem_servico.numero, "OS-P-01")
