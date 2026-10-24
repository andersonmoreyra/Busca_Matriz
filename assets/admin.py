from django.contrib import admin
from .models import CentroCusto, Local, Ativo

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
    list_display = ('codigo_patrimonio', 'nome', 'status', 'local', 'centro_custo', 'ativo_pai')
    list_filter = ('status', 'local', 'centro_custo', 'fabricante')
    search_fields = ('codigo_patrimonio', 'nome', 'numero_serie', 'fabricante', 'modelo')
