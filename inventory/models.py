from django.db import models
from assets.models import Local

class Armazem(models.Model):
    codigo = models.CharField(max_length=50, unique=True, verbose_name="Código do Armazém")
    nome = models.CharField(max_length=255, verbose_name="Nome")
    local = models.ForeignKey(Local, on_delete=models.SET_NULL, null=True, blank=True, related_name='armazens', verbose_name="Localidade")

    def __str__(self):
        return f"{self.codigo} - {self.nome}"

    class Meta:
        verbose_name = "Armazém"
        verbose_name_plural = "Armazéns"


class Peca(models.Model):
    codigo_sku = models.CharField(max_length=100, unique=True, verbose_name="SKU / Código da Peça")
    descricao = models.CharField(max_length=255, verbose_name="Descrição")
    fabricante = models.CharField(max_length=255, blank=True, null=True, verbose_name="Fabricante")
    categoria = models.CharField(max_length=100, choices=[
        ('mecanica', 'Mecânica'),
        ('eletrica', 'Elétrica'),
        ('hidraulica', 'Hidráulica'),
        ('lubrificante', 'Lubrificante/Químico'),
        ('epi', 'EPI / Segurança'),
        ('outros', 'Outros')
    ], default='mecanica', verbose_name="Categoria")

    estoque_minimo = models.IntegerField(default=1, verbose_name="Estoque Mínimo")
    estoque_maximo = models.IntegerField(default=10, verbose_name="Estoque Máximo")
    custo_unitario = models.DecimalField(max_digits=10, decimal_places=2, default=0.00, verbose_name="Custo Unitário Padrão")

    def __str__(self):
        return f"{self.codigo_sku} - {self.descricao}"

    class Meta:
        verbose_name = "Peça/Material"
        verbose_name_plural = "Peças e Materiais"


class Estoque(models.Model):
    armazem = models.ForeignKey(Armazem, on_delete=models.CASCADE, related_name='estoques', verbose_name="Armazém")
    peca = models.ForeignKey(Peca, on_delete=models.CASCADE, related_name='estoques_locais', verbose_name="Peça")
    quantidade = models.IntegerField(default=0, verbose_name="Quantidade Atual")
    prateleira_localizacao = models.CharField(max_length=100, blank=True, null=True, verbose_name="Localização (Corredor/Prateleira)")

    def __str__(self):
        return f"{self.peca.descricao} no {self.armazem.nome}: {self.quantidade} un"

    class Meta:
        unique_together = ('armazem', 'peca')
        verbose_name = "Saldo de Estoque"
        verbose_name_plural = "Saldos de Estoque"


class MovimentacaoEstoque(models.Model):
    peca = models.ForeignKey(Peca, on_delete=models.CASCADE, related_name='movimentacoes', verbose_name="Peça")
    armazem = models.ForeignKey(Armazem, on_delete=models.CASCADE, related_name='movimentacoes', verbose_name="Armazém")
    tipo = models.CharField(max_length=50, choices=[
        ('entrada', 'Entrada (Recebimento)'),
        ('saida', 'Saída (Consumo/OS)'),
        ('ajuste', 'Ajuste de Inventário'),
    ], verbose_name="Tipo de Movimentação")

    quantidade = models.IntegerField(verbose_name="Quantidade")
    data_movimentacao = models.DateTimeField(auto_now_add=True, verbose_name="Data da Movimentação")
    referencia = models.CharField(max_length=255, blank=True, null=True, verbose_name="Referência (OS, Nota Fiscal, etc.)")

    def __str__(self):
        return f"{self.get_tipo_display()} de {self.quantidade}x {self.peca.codigo_sku} em {self.data_movimentacao.strftime('%d/%m/%Y')}"

    class Meta:
        verbose_name = "Movimentação de Estoque"
        verbose_name_plural = "Movimentações de Estoque"
