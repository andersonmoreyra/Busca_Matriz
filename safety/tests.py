from django.test import TestCase
from django.utils import timezone
from assets.models import Ativo
from orders.models import SolicitacaoManutencao, OrdemServico
from .models import PermissaoTrabalho, IsolamentoLOTO
from datetime import timedelta

class SafetyTest(TestCase):
    def setUp(self):
        self.ativo = Ativo.objects.create(nome="Painel Elétrico Principal", codigo_patrimonio="PNL-01")
        self.solicitacao = SolicitacaoManutencao.objects.create(ativo=self.ativo, descricao="Falha")
        self.os = OrdemServico.objects.create(numero="OS-S-01", ativo=self.ativo, solicitacao_origem=self.solicitacao, descricao="Manutenção no painel")

        self.permissao = PermissaoTrabalho.objects.create(
            ordem_servico=self.os,
            eletricidade=True,
            valido_ate=timezone.now() + timedelta(hours=8),
            status="aprovada"
        )

        self.loto = IsolamentoLOTO.objects.create(
            permissao=self.permissao,
            ativo=self.ativo,
            ponto_bloqueio="Chave Geral",
            tipo_energia="eletrica",
            data_aplicacao=timezone.now()
        )

    def test_permissao_trabalho(self):
        self.assertTrue(self.permissao.eletricidade)
        self.assertFalse(self.permissao.trabalho_altura)
        self.assertEqual(self.permissao.status, "aprovada")

    def test_loto(self):
        self.assertEqual(self.loto.tipo_energia, "eletrica")
        self.assertEqual(self.loto.ponto_bloqueio, "Chave Geral")
        self.assertEqual(self.loto.permissao.ordem_servico.numero, "OS-S-01")
