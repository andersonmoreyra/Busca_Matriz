from django.contrib import admin
from .models import PlanoManutencao, GatilhoManutencao, TarefaPreventiva

class GatilhoManutencaoInline(admin.TabularInline):
    model = GatilhoManutencao
    extra = 1

class TarefaPreventivaInline(admin.TabularInline):
    model = TarefaPreventiva
    extra = 1

@admin.register(PlanoManutencao)
class PlanoManutencaoAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'ativo', 'ativo_status', 'criado_em')
    list_filter = ('ativo_status', 'criado_em')
    search_fields = ('titulo', 'ativo__nome')
    inlines = [GatilhoManutencaoInline, TarefaPreventivaInline]

@admin.register(GatilhoManutencao)
class GatilhoManutencaoAdmin(admin.ModelAdmin):
    list_display = ('plano', 'tipo', 'valor_referencia', 'unidade_medida')
    list_filter = ('tipo',)
    search_fields = ('plano__titulo',)

@admin.register(TarefaPreventiva)
class TarefaPreventivaAdmin(admin.ModelAdmin):
    list_display = ('descricao', 'plano', 'ordem_execucao', 'tempo_estimado_minutos')
    list_filter = ('plano',)
    search_fields = ('descricao', 'plano__titulo')
