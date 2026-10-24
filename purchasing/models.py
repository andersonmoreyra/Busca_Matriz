from django.db import models
from inventory.models import Peca
from django.contrib.auth.models import User

class Fornecedor(models.Model):
    cnpj = models.CharField(max_length=20, unique=True, verbose_name="CNPJ")
    razao_social = models.CharField(max_length=255, verbose_name="Razão Social")
    nome_fantasia = models.CharField(max_length=255, blank=True, null=True, verbose_name="Nome Fantasia")
    contato_nome = models.CharField(max_length=255, blank=True, null=True, verbose_name="Nome do Contato")
    email = models.EmailField(blank=True, null=True, verbose_name="E-mail")
    telefone = models.CharField(max_length=50, blank=True, null=True, verbose_name="Telefone")

    ativo = models.BooleanField(default=True, verbose_name="Fornecedor Ativo")

    def __str__(self):
        return self.nome_fantasia if self.nome_fantasia else self.razao_social

    class Meta:
        verbose_name = "Fornecedor"
        verbose_name_plural = "Fornecedores"


class SolicitacaoCompra(models.Model):
    solicitante = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='compras_solicitadas', verbose_name="Solicitante")
    data_solicitacao = models.DateTimeField(auto_now_add=True, verbose_name="Data da Solicitação")
    justificativa = models.TextField(verbose_name="Justificativa da Compra")

    status = models.CharField(max_length=50, choices=[
        ('pendente', 'Pendente de Aprovação'),
        ('aprovada', 'Aprovada / Aguardando Cotação'),
        ('em_cotacao', 'Em Cotação'),
        ('pedido_gerado', 'Pedido Gerado'),
        ('cancelada', 'Cancelada'),
    ], default='pendente', verbose_name="Status")

    def __str__(self):
        return f"SC #{self.id} - {self.get_status_display()}"

    class Meta:
        verbose_name = "Solicitação de Compra"
        verbose_name_plural = "Solicitações de Compra"


class ItemSolicitacaoCompra(models.Model):
    solicitacao = models.ForeignKey(SolicitacaoCompra, on_delete=models.CASCADE, related_name='itens', verbose_name="Solicitação")
    peca = models.ForeignKey(Peca, on_delete=models.SET_NULL, null=True, blank=True, verbose_name="Peça/Material (Catalogo)")
    descricao_livre = models.CharField(max_length=255, blank=True, null=True, verbose_name="Descrição (Material sem cadastro)")
    quantidade = models.IntegerField(verbose_name="Quantidade")

    def __str__(self):
        desc = self.peca.descricao if self.peca else self.descricao_livre
        return f"{self.quantidade}x {desc} (SC #{self.solicitacao.id})"

    class Meta:
        verbose_name = "Item da SC"
        verbose_name_plural = "Itens da SC"


class PedidoCompra(models.Model):
    numero = models.CharField(max_length=50, unique=True, verbose_name="Número do Pedido")
    fornecedor = models.ForeignKey(Fornecedor, on_delete=models.CASCADE, related_name='pedidos', verbose_name="Fornecedor")
    solicitacao_origem = models.ForeignKey(SolicitacaoCompra, on_delete=models.SET_NULL, null=True, blank=True, related_name='pedidos', verbose_name="Solicitação Origem")

    data_emissao = models.DateField(auto_now_add=True, verbose_name="Data de Emissão")
    data_prevista_entrega = models.DateField(blank=True, null=True, verbose_name="Previsão de Entrega")

    valor_total = models.DecimalField(max_digits=12, decimal_places=2, default=0.00, verbose_name="Valor Total")

    status = models.CharField(max_length=50, choices=[
        ('emitido', 'Emitido'),
        ('enviado', 'Enviado ao Fornecedor'),
        ('parcial', 'Recebido Parcialmente'),
        ('entregue', 'Entregue / Concluído'),
        ('cancelado', 'Cancelado')
    ], default='emitido', verbose_name="Status")

    def __str__(self):
        return f"PC {self.numero} - {self.fornecedor} ({self.get_status_display()})"

    class Meta:
        verbose_name = "Pedido de Compra"
        verbose_name_plural = "Pedidos de Compra"
