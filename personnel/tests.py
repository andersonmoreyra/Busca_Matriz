from django.test import TestCase
from django.contrib.auth.models import User
from assets.models import Ativo, CentroCusto, Local
from orders.models import OrdemServico, SolicitacaoManutencao
from .models import Especialidade, Equipe, Funcionario, ApontamentoHoras

class PersonnelTest(TestCase):
    def setUp(self):
        self.user_supervisor = User.objects.create_user(username='supervisor', password='123')
        self.user_tecnico = User.objects.create_user(username='tecnico', password='123')

        self.especialidade = Especialidade.objects.create(nome="Mecânico Industrial")

        self.equipe = Equipe.objects.create(
            nome="Equipe Alpha",
            supervisor=self.user_supervisor
        )

        self.funcionario = Funcionario.objects.create(
            usuario=self.user_tecnico,
            matricula="MAT-001",
            equipe=self.equipe,
            especialidade=self.especialidade,
            valor_hora=35.50
        )

        # Criar dependências para OS
        self.centro = CentroCusto.objects.create(codigo="C1", descricao="D1")
        self.local = Local.objects.create(nome="L1")
        self.ativo = Ativo.objects.create(nome="A1", codigo_patrimonio="P1", centro_custo=self.centro, local=self.local)
        self.solicitacao = SolicitacaoManutencao.objects.create(ativo=self.ativo, descricao="D")
        self.os = OrdemServico.objects.create(numero="OS-01", ativo=self.ativo, solicitacao_origem=self.solicitacao, descricao="Desc")

        self.apontamento = ApontamentoHoras.objects.create(
            ordem_servico=self.os,
            funcionario=self.funcionario,
            data_trabalho="2023-10-01",
            hora_inicio="08:00:00",
            hora_fim="12:00:00",
            descricao="Troca de correia"
        )

    def test_especialidade_criacao(self):
        self.assertEqual(self.especialidade.nome, "Mecânico Industrial")

    def test_equipe_criacao(self):
        self.assertEqual(self.equipe.nome, "Equipe Alpha")
        self.assertEqual(self.equipe.supervisor.username, "supervisor")

    def test_funcionario_criacao(self):
        self.assertEqual(self.funcionario.matricula, "MAT-001")
        self.assertEqual(self.funcionario.especialidade.nome, "Mecânico Industrial")

    def test_apontamento_horas(self):
        self.assertEqual(self.apontamento.descricao, "Troca de correia")
        self.assertEqual(self.apontamento.hora_inicio, "08:00:00")
        self.assertEqual(self.apontamento.ordem_servico.numero, "OS-01")
