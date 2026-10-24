from django.test import TestCase
from django.utils import timezone
from assets.models import Ativo
from orders.models import SolicitacaoManutencao, OrdemServico
from .models import ModoFalha, CausaFalha, RegistroOcorrenciaFalha
from datetime import timedelta

class ReliabilityTest(TestCase):
    def setUp(self):
        self.ativo = Ativo.objects.create(nome="Bomba D'água", codigo_patrimonio="BMB-01")
        self.solicitacao = SolicitacaoManutencao.objects.create(ativo=self.ativo, descricao="Falha")
        self.os = OrdemServico.objects.create(numero="OS-R-01", ativo=self.ativo, solicitacao_origem=self.solicitacao, descricao="Reparo na bomba")

        self.modo_falha = ModoFalha.objects.create(codigo="MF-01", descricao="Vazamento")
        self.causa_falha = CausaFalha.objects.create(codigo="CF-01", descricao="Desgaste do Selo")

        now = timezone.now()

        self.ocorrencia = RegistroOcorrenciaFalha.objects.create(
            ordem_servico=self.os,
            ativo=self.ativo,
            modo_falha=self.modo_falha,
            causa_falha=self.causa_falha,
            data_inicio_falha=now - timedelta(hours=2),
            data_fim_falha=now,
            tempo_inatividade_minutos=120
        )

    def test_modo_causa(self):
        self.assertEqual(self.modo_falha.codigo, "MF-01")
        self.assertEqual(self.causa_falha.descricao, "Desgaste do Selo")

    def test_registro_ocorrencia(self):
        self.assertEqual(self.ocorrencia.tempo_inatividade_minutos, 120)
        self.assertEqual(self.ocorrencia.modo_falha.descricao, "Vazamento")
        self.assertEqual(self.ocorrencia.ativo.nome, "Bomba D'água")
