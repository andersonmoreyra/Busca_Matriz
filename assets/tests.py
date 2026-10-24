from django.test import TestCase
from .models import CentroCusto, Local, Ativo

class AtivoModelTest(TestCase):

    def setUp(self):
        self.centro_custo = CentroCusto.objects.create(codigo="CC01", descricao="Manutenção")
        self.local = Local.objects.create(nome="Fábrica 1", descricao="Fábrica principal")
        self.ativo = Ativo.objects.create(
            nome="Torno CNC",
            codigo_patrimonio="PAT-001",
            centro_custo=self.centro_custo,
            local=self.local
        )

    def test_criacao_ativo(self):
        self.assertEqual(self.ativo.nome, "Torno CNC")
        self.assertEqual(self.ativo.status, "operacional")
        self.assertEqual(self.ativo.centro_custo.codigo, "CC01")
        self.assertEqual(self.ativo.local.nome, "Fábrica 1")

    def test_str_centro_custo(self):
        self.assertEqual(str(self.centro_custo), "CC01 - Manutenção")

    def test_str_local(self):
        self.assertEqual(str(self.local), "Fábrica 1")

    def test_str_ativo(self):
        self.assertEqual(str(self.ativo), "PAT-001 - Torno CNC")

    def test_hierarquia_locais(self):
        sublocal = Local.objects.create(nome="Setor de Usinagem", local_pai=self.local)
        self.assertEqual(str(sublocal), "Fábrica 1 > Setor de Usinagem")

    def test_hierarquia_ativos(self):
        subativo = Ativo.objects.create(
            nome="Motor Principal do Torno",
            codigo_patrimonio="PAT-002",
            ativo_pai=self.ativo
        )
        self.assertEqual(subativo.ativo_pai.nome, "Torno CNC")
