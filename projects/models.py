from django.db import models
from assets.models import Local
from orders.models import OrdemServico
from django.contrib.auth.models import User

class ParadaProgramada(models.Model):
    titulo = models.CharField(max_length=255, verbose_name="Título da Parada/Projeto")
    descricao = models.TextField(blank=True, null=True, verbose_name="Escopo")
    local_afetado = models.ForeignKey(Local, on_delete=models.SET_NULL, null=True, blank=True, verbose_name="Local / Área Afetada")

    coordenador = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='paradas_coordenadas', verbose_name="Coordenador Geral")

    data_inicio_prevista = models.DateField(verbose_name="Início Previsto")
    data_fim_prevista = models.DateField(verbose_name="Fim Previsto")

    data_inicio_real = models.DateField(blank=True, null=True, verbose_name="Início Real")
    data_fim_real = models.DateField(blank=True, null=True, verbose_name="Fim Real")

    orcamento_aprovado = models.DecimalField(max_digits=12, decimal_places=2, default=0.00, verbose_name="Orçamento Aprovado")

    status = models.CharField(max_length=50, choices=[
        ('planejamento', 'Em Planejamento'),
        ('aprovada', 'Aprovada'),
        ('em_andamento', 'Em Andamento'),
        ('concluida', 'Concluída'),
        ('cancelada', 'Cancelada')
    ], default='planejamento', verbose_name="Status")

    def __str__(self):
        return f"{self.titulo} ({self.get_status_display()})"

    class Meta:
        verbose_name = "Parada Programada / Projeto"
        verbose_name_plural = "Paradas Programadas e Projetos"


class VinculoParadaOS(models.Model):
    parada = models.ForeignKey(ParadaProgramada, on_delete=models.CASCADE, related_name='ordens_vinculadas', verbose_name="Parada Programada")
    ordem_servico = models.OneToOneField(OrdemServico, on_delete=models.CASCADE, related_name='parada_associada', verbose_name="Ordem de Serviço")

    def __str__(self):
        return f"OS {self.ordem_servico.numero} -> {self.parada.titulo}"

    class Meta:
        verbose_name = "Vínculo de OS na Parada"
        verbose_name_plural = "Vínculos de OS na Parada"
