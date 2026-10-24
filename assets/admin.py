from django.contrib import admin
from .models import CentroCusto, Local, Ativo, Componente, DocumentoTecnico, Garantia

class ComponenteInline(admin.TabularInline):
    model = Componente
    extra = 1

class DocumentoTecnicoInline(admin.TabularInline):
    model = DocumentoTecnico
    extra = 1

class GarantiaInline(admin.StackedInline):
    model = Garantia
    can_delete = False

@admin.register(CentroCusto)
class CentroCustoAdmin(admin.ModelAdmin):
    list_display = ('codigo', 'descricao')
    search_fields = ('codigo', 'descricao')

@admin.register(Local)
class LocalAdmin(admin.ModelAdmin):
    list_display = ('nome', 'local_pai')
    search_fields = ('nome',)
    list_filter = ('local_pai',)

@admin.register(Ativo)
class AtivoAdmin(admin.ModelAdmin):
    list_display = ('codigo_patrimonio', 'nome', 'status', 'criticidade', 'local', 'centro_custo')
    list_filter = ('status', 'criticidade', 'local', 'centro_custo', 'fabricante')
    search_fields = ('codigo_patrimonio', 'nome', 'numero_serie', 'fabricante', 'modelo')
    inlines = [GarantiaInline, ComponenteInline, DocumentoTecnicoInline]

@admin.register(Componente)
class ComponenteAdmin(admin.ModelAdmin):
    list_display = ('nome', 'ativo', 'numero_peca')
    search_fields = ('nome', 'numero_peca', 'ativo__nome')

@admin.register(DocumentoTecnico)
class DocumentoTecnicoAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'tipo', 'ativo')
    list_filter = ('tipo',)
    search_fields = ('titulo', 'ativo__nome')

@admin.register(Garantia)
class GarantiaAdmin(admin.ModelAdmin):
    list_display = ('ativo', 'fornecedor', 'data_fim')
    search_fields = ('ativo__nome', 'fornecedor')
