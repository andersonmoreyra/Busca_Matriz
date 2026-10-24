from django.test import TestCase
from django.contrib.auth.models import User
from inventory.models import Peca
from .models import Fornecedor, SolicitacaoCompra, ItemSolicitacaoCompra, PedidoCompra

class PurchasingTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='comprador', password='123')
        self.fornecedor = Fornecedor.objects.create(
            cnpj="12.345.678/0001-90",
            razao_social="Fornecedor de Peças SA",
            nome_fantasia="Peças SA"
        )

        self.peca = Peca.objects.create(
            codigo_sku="FILTRO-01",
            descricao="Filtro de Ar",
            categoria="mecanica"
        )

        self.solicitacao = SolicitacaoCompra.objects.create(
            solicitante=self.user,
            justificativa="Reposição de estoque"
        )

        self.item_sc = ItemSolicitacaoCompra.objects.create(
            solicitacao=self.solicitacao,
            peca=self.peca,
            quantidade=20
        )

        self.pedido = PedidoCompra.objects.create(
            numero="PC-2023-100",
            fornecedor=self.fornecedor,
            solicitacao_origem=self.solicitacao,
            valor_total=500.00
        )

    def test_fornecedor_criacao(self):
        self.assertEqual(self.fornecedor.cnpj, "12.345.678/0001-90")

    def test_solicitacao_compra(self):
        self.assertEqual(self.solicitacao.justificativa, "Reposição de estoque")
        self.assertEqual(self.solicitacao.status, "pendente")

    def test_item_solicitacao(self):
        self.assertEqual(self.item_sc.quantidade, 20)
        self.assertEqual(self.item_sc.peca.codigo_sku, "FILTRO-01")

    def test_pedido_compra(self):
        self.assertEqual(self.pedido.numero, "PC-2023-100")
        self.assertEqual(self.pedido.fornecedor.nome_fantasia, "Peças SA")
        self.assertEqual(self.pedido.valor_total, 500.00)
