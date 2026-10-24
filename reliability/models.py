from django.db import models
from assets.models import Ativo
from orders.models import OrdemServico

class ModoFalha(models.Model):
    codigo = models.CharField(max_length=50, unique=True, verbose_name="Código")
    descricao = models.CharField(max_length=255, verbose_name="Modo de Falha (Sintoma)")

    def __str__(self):
        return f"{self.codigo} - {self.descricao}"

    class Meta:
        verbose_name = "Modo de Falha"
        verbose_name_plural = "Modos de Falha"


class CausaFalha(models.Model):
    codigo = models.CharField(max_length=50, unique=True, verbose_name="Código")
    descricao = models.CharField(max_length=255, verbose_name="Causa Raiz da Falha")

    def __str__(self):
        return f"{self.codigo} - {self.descricao}"

    class Meta:
        verbose_name = "Causa da Falha"
        verbose_name_plural = "Causas de Falhas"


class RegistroOcorrenciaFalha(models.Model):
    ordem_servico = models.OneToOneField(OrdemServico, on_delete=models.CASCADE, related_name='analise_falha', verbose_name="Ordem de Serviço")
    ativo = models.ForeignKey(Ativo, on_delete=models.CASCADE, related_name='historico_falhas', verbose_name="Ativo")

    modo_falha = models.ForeignKey(ModoFalha, on_delete=models.SET_NULL, null=True, blank=True, verbose_name="Sintoma/Modo")
    causa_falha = models.ForeignKey(CausaFalha, on_delete=models.SET_NULL, null=True, blank=True, verbose_name="Causa Raiz")

    data_inicio_falha = models.DateTimeField(verbose_name="Data/Hora Início da Falha")
    data_fim_falha = models.DateTimeField(verbose_name="Data/Hora Fim da Falha (Retorno à Operação)")

    houve_parada_producao = models.BooleanField(default=True, verbose_name="Houve Parada de Produção?")
    tempo_inatividade_minutos = models.IntegerField(verbose_name="Tempo de Inatividade (minutos)")

    acao_corretiva_aplicada = models.TextField(blank=True, null=True, verbose_name="Ação Corretiva Imediata")
    acao_preventiva_recomendada = models.TextField(blank=True, null=True, verbose_name="Ação Preventiva (Bloqueio de Causa)")

    def __str__(self):
        return f"Falha na OS {self.ordem_servico.numero} - Ativo: {self.ativo.nome}"

    class Meta:
        verbose_name = "Registro de Ocorrência de Falha"
        verbose_name_plural = "Registros de Ocorrências de Falhas"
