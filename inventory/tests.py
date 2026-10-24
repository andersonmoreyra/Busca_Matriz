from django.test import TestCase
from assets.models import Local
from .models import Armazem, Peca, Estoque, MovimentacaoEstoque

class InventoryTest(TestCase):
    def setUp(self):
        self.local = Local.objects.create(nome="Almoxarifado Central")
        self.armazem = Armazem.objects.create(codigo="ARM-01", nome="Almoxarifado Peças", local=self.local)

        self.peca = Peca.objects.create(
            codigo_sku="ROL-6204",
            descricao="Rolamento SKF 6204",
            categoria="mecanica",
            estoque_minimo=5,
            estoque_maximo=50,
            custo_unitario=25.50
        )

        self.estoque = Estoque.objects.create(
            armazem=self.armazem,
            peca=self.peca,
            quantidade=10,
            prateleira_localizacao="A-01"
        )

        self.movimentacao = MovimentacaoEstoque.objects.create(
            peca=self.peca,
            armazem=self.armazem,
            tipo="entrada",
            quantidade=10,
            referencia="NF 12345"
        )

    def test_armazem_criacao(self):
        self.assertEqual(self.armazem.codigo, "ARM-01")

    def test_peca_criacao(self):
        self.assertEqual(self.peca.codigo_sku, "ROL-6204")
        self.assertEqual(self.peca.custo_unitario, 25.50)

    def test_estoque_relacionamento(self):
        self.assertEqual(self.estoque.peca.descricao, "Rolamento SKF 6204")
        self.assertEqual(self.estoque.quantidade, 10)

    def test_movimentacao_estoque(self):
        self.assertEqual(self.movimentacao.tipo, "entrada")
        self.assertEqual(self.movimentacao.quantidade, 10)
