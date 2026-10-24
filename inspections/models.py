from django.db import models
from assets.models import Ativo

class RoteiroInspecao(models.Model):
    titulo = models.CharField(max_length=255, verbose_name="Título do Roteiro")
    descricao = models.TextField(blank=True, null=True, verbose_name="Descrição/Objetivo")
    frequencia = models.CharField(max_length=50, choices=[
        ('diaria', 'Diária'),
        ('semanal', 'Semanal'),
        ('mensal', 'Mensal'),
        ('anual', 'Anual')
    ], default='mensal', verbose_name="Frequência Base")

    def __str__(self):
        return self.titulo

    class Meta:
        verbose_name = "Roteiro de Inspeção"
        verbose_name_plural = "Roteiros de Inspeção"


class ChecklistItem(models.Model):
    roteiro = models.ForeignKey(RoteiroInspecao, on_delete=models.CASCADE, related_name='itens', verbose_name="Roteiro")
    pergunta = models.CharField(max_length=255, verbose_name="Critério / Pergunta")
    tipo_resposta = models.CharField(max_length=50, choices=[
        ('ok_nok', 'OK / Não OK'),
        ('numero', 'Valor Numérico'),
        ('texto', 'Texto Livre')
    ], default='ok_nok', verbose_name="Tipo de Resposta Esperada")
    obrigatorio = models.BooleanField(default=True, verbose_name="Obrigatório")

    def __str__(self):
        return f"{self.pergunta} ({self.get_tipo_resposta_display()})"

    class Meta:
        verbose_name = "Item do Checklist"
        verbose_name_plural = "Itens do Checklist"


class PontoMedicao(models.Model):
    ativo = models.ForeignKey(Ativo, on_delete=models.CASCADE, related_name='pontos_medicao', verbose_name="Ativo")
    nome = models.CharField(max_length=255, verbose_name="Nome do Ponto de Medição (ex: Mancal Traseiro)")
    unidade = models.CharField(max_length=20, verbose_name="Unidade de Medida (ex: °C, mm/s)")
    limite_minimo = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True, verbose_name="Limite Mínimo Aceitável")
    limite_maximo = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True, verbose_name="Limite Máximo Aceitável")

    def __str__(self):
        return f"{self.nome} - {self.ativo.nome}"

    class Meta:
        verbose_name = "Ponto de Medição"
        verbose_name_plural = "Pontos de Medição"


class InstrumentoCalibracao(models.Model):
    ativo_associado = models.OneToOneField(Ativo, on_delete=models.CASCADE, related_name='dados_calibracao', verbose_name="Ativo (Instrumento)")
    frequencia_meses = models.IntegerField(default=12, verbose_name="Frequência de Calibração (meses)")
    ultima_calibracao = models.DateField(blank=True, null=True, verbose_name="Data da Última Calibração")
    proxima_calibracao = models.DateField(blank=True, null=True, verbose_name="Data da Próxima Calibração")
    certificado = models.CharField(max_length=100, blank=True, null=True, verbose_name="Número do Certificado")

    def __str__(self):
        return f"Calibração: {self.ativo_associado.nome} (Vence em {self.proxima_calibracao})"

    class Meta:
        verbose_name = "Instrumento de Calibração"
        verbose_name_plural = "Instrumentos de Calibração"
