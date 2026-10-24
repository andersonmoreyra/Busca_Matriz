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

    criticidade = models.CharField(max_length=50, choices=[
        ('baixa', 'Baixa'),
        ('media', 'Média'),
        ('alta', 'Alta'),
        ('critica', 'Crítica')
    ], default='baixa', verbose_name="Criticidade")

    def __str__(self):
        return f"{self.codigo_patrimonio} - {self.nome}"

    class Meta:
        verbose_name = "Ativo"
        verbose_name_plural = "Ativos"


class Componente(models.Model):
    ativo = models.ForeignKey(Ativo, on_delete=models.CASCADE, related_name='componentes', verbose_name="Ativo")
    nome = models.CharField(max_length=255, verbose_name="Nome do Componente")
    descricao = models.TextField(blank=True, null=True, verbose_name="Descrição")
    numero_peca = models.CharField(max_length=100, blank=True, null=True, verbose_name="Número da Peça")

    def __str__(self):
        return f"{self.nome} ({self.ativo.nome})"

    class Meta:
        verbose_name = "Componente"
        verbose_name_plural = "Componentes"


class DocumentoTecnico(models.Model):
    ativo = models.ForeignKey(Ativo, on_delete=models.CASCADE, related_name='documentos', verbose_name="Ativo")
    titulo = models.CharField(max_length=255, verbose_name="Título do Documento")
    tipo = models.CharField(max_length=50, choices=[
        ('manual', 'Manual'),
        ('esquema', 'Esquema Elétrico/Mecânico'),
        ('certificado', 'Certificado'),
        ('fotografia', 'Fotografia'),
        ('outro', 'Outro')
    ], default='manual', verbose_name="Tipo de Documento")
    arquivo = models.FileField(upload_to='documentos_tecnicos/', blank=True, null=True, verbose_name="Arquivo")

    def __str__(self):
        return f"{self.titulo} - {self.ativo.nome}"

    class Meta:
        verbose_name = "Documento Técnico"
        verbose_name_plural = "Documentos Técnicos"


class Garantia(models.Model):
    ativo = models.OneToOneField(Ativo, on_delete=models.CASCADE, related_name='garantia', verbose_name="Ativo")
    fornecedor = models.CharField(max_length=255, verbose_name="Fornecedor")
    data_inicio = models.DateField(verbose_name="Data de Início")
    data_fim = models.DateField(verbose_name="Data de Término")
    cobertura = models.TextField(blank=True, null=True, verbose_name="Detalhes da Cobertura")

    def __str__(self):
        return f"Garantia {self.ativo.nome} - Vence: {self.data_fim}"

    class Meta:
        verbose_name = "Garantia"
        verbose_name_plural = "Garantias"
