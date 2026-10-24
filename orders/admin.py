from django.contrib import admin
from .models import SolicitacaoManutencao, OrdemServico, TarefaOS

@admin.register(SolicitacaoManutencao)
class SolicitacaoManutencaoAdmin(admin.ModelAdmin):
    list_display = ('id', 'ativo', 'urgencia', 'status', 'solicitante', 'data_solicitacao')
    list_filter = ('status', 'urgencia', 'data_solicitacao')
    search_fields = ('ativo__nome', 'descricao', 'solicitante__username')

class TarefaOSInline(admin.TabularInline):
    model = TarefaOS
    extra = 1

@admin.register(OrdemServico)
class OrdemServicoAdmin(admin.ModelAdmin):
    list_display = ('numero', 'ativo', 'tipo_manutencao', 'prioridade', 'status', 'responsavel')
    list_filter = ('status', 'tipo_manutencao', 'prioridade', 'data_criacao')
    search_fields = ('numero', 'ativo__nome', 'descricao', 'responsavel__username')
    inlines = [TarefaOSInline]

@admin.register(TarefaOS)
class TarefaOSAdmin(admin.ModelAdmin):
    list_display = ('descricao', 'ordem_servico', 'concluida')
    list_filter = ('concluida',)
    search_fields = ('descricao', 'ordem_servico__numero')
