from django.db import models
from assets.models import Ativo

class PlanoManutencao(models.Model):
    titulo = models.CharField(max_length=255, verbose_name="Título do Plano")
    descricao = models.TextField(blank=True, null=True, verbose_name="Descrição do Plano")
    ativo = models.ForeignKey(Ativo, on_delete=models.CASCADE, related_name='planos_manutencao', verbose_name="Ativo Associado")
    ativo_status = models.BooleanField(default=True, verbose_name="Plano Ativo")

    criado_em = models.DateTimeField(auto_now_add=True)
    atualizado_em = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.titulo} - {self.ativo.nome}"

    class Meta:
        verbose_name = "Plano de Manutenção"
        verbose_name_plural = "Planos de Manutenção"


class GatilhoManutencao(models.Model):
    plano = models.ForeignKey(PlanoManutencao, on_delete=models.CASCADE, related_name='gatilhos', verbose_name="Plano de Manutenção")
    tipo = models.CharField(max_length=50, choices=[
        ('tempo', 'Baseado em Tempo (Dias/Meses)'),
        ('uso', 'Baseado em Uso (Horas/Km/Ciclos)'),
        ('condicao', 'Baseado em Condição (Limites)'),
    ], default='tempo', verbose_name="Tipo de Gatilho")

    valor_referencia = models.IntegerField(verbose_name="Valor de Referência (ex: 30 dias, 1000 horas)")
    unidade_medida = models.CharField(max_length=50, blank=True, null=True, verbose_name="Unidade (ex: dias, horas, km)")

    def __str__(self):
        return f"Gatilho: {self.valor_referencia} {self.unidade_medida} ({self.get_tipo_display()})"

    class Meta:
        verbose_name = "Gatilho de Manutenção"
        verbose_name_plural = "Gatilhos de Manutenção"


class TarefaPreventiva(models.Model):
    plano = models.ForeignKey(PlanoManutencao, on_delete=models.CASCADE, related_name='tarefas_preventivas', verbose_name="Plano de Manutenção")
    descricao = models.CharField(max_length=255, verbose_name="Descrição da Tarefa")
    ordem_execucao = models.IntegerField(default=1, verbose_name="Ordem de Execução")
    tempo_estimado_minutos = models.IntegerField(default=30, verbose_name="Tempo Estimado (min)")

    def __str__(self):
        return f"{self.ordem_execucao} - {self.descricao}"

    class Meta:
        ordering = ['ordem_execucao']
        verbose_name = "Tarefa Preventiva"
        verbose_name_plural = "Tarefas Preventivas"
