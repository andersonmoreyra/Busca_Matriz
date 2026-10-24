from django.test import TestCase
from django.contrib.auth.models import User
from assets.models import Ativo, CentroCusto, Local
from .models import SolicitacaoManutencao, OrdemServico, TarefaOS

class OrdemServicoModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='tecnico', password='123')
        self.centro_custo = CentroCusto.objects.create(codigo="CC02", descricao="Produção")
        self.local = Local.objects.create(nome="Fábrica 2")
        self.ativo = Ativo.objects.create(
            nome="Prensa Hidráulica",
            codigo_patrimonio="PAT-003",
            centro_custo=self.centro_custo,
            local=self.local
        )

        self.solicitacao = SolicitacaoManutencao.objects.create(
            ativo=self.ativo,
            solicitante=self.user,
            descricao="Vazamento de óleo",
            urgencia="alta"
        )

        self.os = OrdemServico.objects.create(
            numero="OS-2023-001",
            solicitacao_origem=self.solicitacao,
            ativo=self.ativo,
            descricao="Troca de retentores",
            tipo_manutencao="corretiva",
            responsavel=self.user
        )

        self.tarefa = TarefaOS.objects.create(
            ordem_servico=self.os,
            descricao="Desmontar cilindro"
        )

    def test_criacao_solicitacao(self):
        self.assertEqual(self.solicitacao.descricao, "Vazamento de óleo")
        self.assertEqual(self.solicitacao.status, "pendente")

    def test_criacao_os(self):
        self.assertEqual(self.os.numero, "OS-2023-001")
        self.assertEqual(self.os.ativo.nome, "Prensa Hidráulica")
        self.assertEqual(self.os.status, "aberta")

    def test_criacao_tarefa(self):
        self.assertEqual(self.tarefa.ordem_servico.numero, "OS-2023-001")
        self.assertFalse(self.tarefa.concluida)
