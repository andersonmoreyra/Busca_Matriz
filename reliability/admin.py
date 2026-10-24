from django.contrib import admin
from .models import ModoFalha, CausaFalha, RegistroOcorrenciaFalha

@admin.register(ModoFalha)
class ModoFalhaAdmin(admin.ModelAdmin):
    list_display = ('codigo', 'descricao')
    search_fields = ('codigo', 'descricao')

@admin.register(CausaFalha)
class CausaFalhaAdmin(admin.ModelAdmin):
    list_display = ('codigo', 'descricao')
    search_fields = ('codigo', 'descricao')

@admin.register(RegistroOcorrenciaFalha)
class RegistroOcorrenciaFalhaAdmin(admin.ModelAdmin):
    list_display = ('ordem_servico', 'ativo', 'modo_falha', 'causa_falha', 'houve_parada_producao', 'tempo_inatividade_minutos')
    list_filter = ('houve_parada_producao', 'modo_falha', 'causa_falha')
    search_fields = ('ordem_servico__numero', 'ativo__nome')
    date_hierarchy = 'data_inicio_falha'
