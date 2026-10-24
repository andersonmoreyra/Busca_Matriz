from django.test import TestCase
from assets.models import Ativo, Local
from .models import RoteiroInspecao, ChecklistItem, PontoMedicao, InstrumentoCalibracao

class InspectionsTest(TestCase):
    def setUp(self):
        self.local = Local.objects.create(nome="Área de Utilidades")
        self.ativo = Ativo.objects.create(nome="Compressor de Ar", codigo_patrimonio="COMP-01", local=self.local)

        self.roteiro = RoteiroInspecao.objects.create(
            titulo="Inspeção Mensal Compressor",
            frequencia="mensal"
        )

        self.item_checklist = ChecklistItem.objects.create(
            roteiro=self.roteiro,
            pergunta="Nível de Óleo OK?",
            tipo_resposta="ok_nok"
        )

        self.ponto_medicao = PontoMedicao.objects.create(
            ativo=self.ativo,
            nome="Vibração Mancal",
            unidade="mm/s",
            limite_maximo=5.50
        )

        self.calibracao = InstrumentoCalibracao.objects.create(
            ativo_associado=self.ativo,
            frequencia_meses=12,
            certificado="CERT-2023"
        )

    def test_roteiro_criacao(self):
        self.assertEqual(self.roteiro.frequencia, "mensal")
        self.assertEqual(self.item_checklist.roteiro.titulo, "Inspeção Mensal Compressor")

    def test_ponto_medicao(self):
        self.assertEqual(self.ponto_medicao.unidade, "mm/s")
        self.assertEqual(self.ponto_medicao.limite_maximo, 5.50)

    def test_instrumento_calibracao(self):
        self.assertEqual(self.calibracao.certificado, "CERT-2023")
