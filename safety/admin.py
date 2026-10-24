from django.contrib import admin
from .models import PermissaoTrabalho, IsolamentoLOTO

class IsolamentoLOTOInline(admin.TabularInline):
    model = IsolamentoLOTO
    extra = 1

@admin.register(PermissaoTrabalho)
class PermissaoTrabalhoAdmin(admin.ModelAdmin):
    list_display = ('ordem_servico', 'status', 'emitente', 'valido_ate', 'trabalho_altura', 'espaco_confinado')
    list_filter = ('status', 'trabalho_altura', 'espaco_confinado', 'trabalho_quente')
    search_fields = ('ordem_servico__numero', 'emitente__username')
    inlines = [IsolamentoLOTOInline]

@admin.register(IsolamentoLOTO)
class IsolamentoLOTOAdmin(admin.ModelAdmin):
    list_display = ('ponto_bloqueio', 'ativo', 'tipo_energia', 'permissao', 'data_aplicacao', 'data_remocao')
    list_filter = ('tipo_energia',)
    search_fields = ('ponto_bloqueio', 'ativo__nome', 'permissao__ordem_servico__numero')
