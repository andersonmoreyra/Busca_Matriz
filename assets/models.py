from django.db import models

class CentroCusto(models.Model):
    codigo = models.CharField(max_length=50, unique=True, verbose_name="Código do Centro de Custo")
    descricao = models.CharField(max_length=255, verbose_name="Descrição")

    def __str__(self):
        return f"{self.codigo} - {self.descricao}"

    class Meta:
        verbose_name = "Centro de Custo"
        verbose_name_plural = "Centros de Custo"


class Local(models.Model):
    nome = models.CharField(max_length=255, verbose_name="Nome do Local")
    descricao = models.TextField(blank=True, null=True, verbose_name="Descrição")
    local_pai = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='sublocais', verbose_name="Local Pai")

    def __str__(self):
        if self.local_pai:
            return f"{self.local_pai.nome} > {self.nome}"
        return self.nome

    class Meta:
        verbose_name = "Local"
        verbose_name_plural = "Locais"


class Ativo(models.Model):
    nome = models.CharField(max_length=255, verbose_name="Nome do Ativo")
    descricao = models.TextField(blank=True, null=True, verbose_name="Descrição")
    codigo_patrimonio = models.CharField(max_length=100, unique=True, verbose_name="Código de Patrimônio")
    numero_serie = models.CharField(max_length=100, blank=True, null=True, verbose_name="Número de Série")
    fabricante = models.CharField(max_length=255, blank=True, null=True, verbose_name="Fabricante")
    modelo = models.CharField(max_length=255, blank=True, null=True, verbose_name="Modelo")

    data_aquisicao = models.DateField(blank=True, null=True, verbose_name="Data de Aquisição")
    data_instalacao = models.DateField(blank=True, null=True, verbose_name="Data de Instalação")

    ativo_pai = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='subativos', verbose_name="Ativo Pai")
    local = models.ForeignKey(Local, on_delete=models.SET_NULL, null=True, blank=True, related_name='ativos', verbose_name="Local")
    centro_custo = models.ForeignKey(CentroCusto, on_delete=models.SET_NULL, null=True, blank=True, related_name='ativos', verbose_name="Centro de Custo")

    status = models.CharField(max_length=50, choices=[
        ('operacional', 'Em Operação'),
        ('manutencao', 'Em Manutenção'),
        ('reserva', 'Reserva'),
        ('desativado', 'Desativado'),
    ], default='operacional', verbose_name="Status")

    def __str__(self):
        return f"{self.codigo_patrimonio} - {self.nome}"

    class Meta:
        verbose_name = "Ativo"
        verbose_name_plural = "Ativos"
