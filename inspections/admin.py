from django.contrib import admin
from .models import RoteiroInspecao, ChecklistItem, PontoMedicao, InstrumentoCalibracao

class ChecklistItemInline(admin.TabularInline):
    model = ChecklistItem
    extra = 1

@admin.register(RoteiroInspecao)
class RoteiroInspecaoAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'frequencia')
    search_fields = ('titulo',)
    inlines = [ChecklistItemInline]

@admin.register(PontoMedicao)
class PontoMedicaoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'ativo', 'unidade', 'limite_minimo', 'limite_maximo')
    list_filter = ('ativo',)
    search_fields = ('nome', 'ativo__nome')

@admin.register(InstrumentoCalibracao)
class InstrumentoCalibracaoAdmin(admin.ModelAdmin):
    list_display = ('ativo_associado', 'frequencia_meses', 'ultima_calibracao', 'proxima_calibracao', 'certificado')
    list_filter = ('proxima_calibracao',)
    search_fields = ('ativo_associado__nome', 'certificado')
