from django.contrib import admin
from .models import Armazem, Peca, Estoque, MovimentacaoEstoque

class EstoqueInline(admin.TabularInline):
    model = Estoque
    extra = 1

@admin.register(Armazem)
class ArmazemAdmin(admin.ModelAdmin):
    list_display = ('codigo', 'nome', 'local')
    search_fields = ('codigo', 'nome')
    inlines = [EstoqueInline]

@admin.register(Peca)
class PecaAdmin(admin.ModelAdmin):
    list_display = ('codigo_sku', 'descricao', 'categoria', 'estoque_minimo', 'estoque_maximo', 'custo_unitario')
    list_filter = ('categoria', 'fabricante')
    search_fields = ('codigo_sku', 'descricao', 'fabricante')
    inlines = [EstoqueInline]

@admin.register(Estoque)
class EstoqueAdmin(admin.ModelAdmin):
    list_display = ('peca', 'armazem', 'quantidade', 'prateleira_localizacao')
    list_filter = ('armazem',)
    search_fields = ('peca__descricao', 'peca__codigo_sku')

@admin.register(MovimentacaoEstoque)
class MovimentacaoEstoqueAdmin(admin.ModelAdmin):
    list_display = ('tipo', 'peca', 'armazem', 'quantidade', 'data_movimentacao', 'referencia')
    list_filter = ('tipo', 'data_movimentacao', 'armazem')
    search_fields = ('peca__descricao', 'referencia')
