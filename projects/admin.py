from django.contrib import admin
from .models import ParadaProgramada, VinculoParadaOS

class VinculoParadaOSInline(admin.TabularInline):
    model = VinculoParadaOS
    extra = 1

@admin.register(ParadaProgramada)
class ParadaProgramadaAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'status', 'data_inicio_prevista', 'data_fim_prevista', 'coordenador')
    list_filter = ('status', 'data_inicio_prevista')
    search_fields = ('titulo', 'coordenador__username')
    inlines = [VinculoParadaOSInline]

@admin.register(VinculoParadaOS)
class VinculoParadaOSAdmin(admin.ModelAdmin):
    list_display = ('parada', 'ordem_servico')
    search_fields = ('parada__titulo', 'ordem_servico__numero')
