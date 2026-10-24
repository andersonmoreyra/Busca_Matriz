from django.contrib import admin
from .models import Especialidade, Equipe, Funcionario, ApontamentoHoras

@admin.register(Especialidade)
class EspecialidadeAdmin(admin.ModelAdmin):
    list_display = ('nome', 'descricao')
    search_fields = ('nome',)

@admin.register(Equipe)
class EquipeAdmin(admin.ModelAdmin):
    list_display = ('nome', 'supervisor')
    search_fields = ('nome', 'supervisor__username')

@admin.register(Funcionario)
class FuncionarioAdmin(admin.ModelAdmin):
    list_display = ('usuario', 'matricula', 'equipe', 'especialidade', 'valor_hora')
    list_filter = ('equipe', 'especialidade')
    search_fields = ('usuario__username', 'usuario__first_name', 'matricula')

@admin.register(ApontamentoHoras)
class ApontamentoHorasAdmin(admin.ModelAdmin):
    list_display = ('funcionario', 'ordem_servico', 'data_trabalho', 'hora_inicio', 'hora_fim')
    list_filter = ('data_trabalho', 'funcionario', 'ordem_servico')
    search_fields = ('funcionario__usuario__username', 'ordem_servico__numero')
