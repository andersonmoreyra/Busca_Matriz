from django.contrib import admin
from .models import Fornecedor, SolicitacaoCompra, ItemSolicitacaoCompra, PedidoCompra

class ItemSolicitacaoCompraInline(admin.TabularInline):
    model = ItemSolicitacaoCompra
    extra = 1

@admin.register(Fornecedor)
class FornecedorAdmin(admin.ModelAdmin):
    list_display = ('cnpj', 'razao_social', 'nome_fantasia', 'contato_nome', 'ativo')
    list_filter = ('ativo',)
    search_fields = ('cnpj', 'razao_social', 'nome_fantasia')

@admin.register(SolicitacaoCompra)
class SolicitacaoCompraAdmin(admin.ModelAdmin):
    list_display = ('id', 'solicitante', 'status', 'data_solicitacao')
    list_filter = ('status', 'data_solicitacao')
    search_fields = ('solicitante__username', 'justificativa')
    inlines = [ItemSolicitacaoCompraInline]

@admin.register(PedidoCompra)
class PedidoCompraAdmin(admin.ModelAdmin):
    list_display = ('numero', 'fornecedor', 'status', 'data_emissao', 'data_prevista_entrega', 'valor_total')
    list_filter = ('status', 'data_emissao', 'fornecedor')
    search_fields = ('numero', 'fornecedor__razao_social')
