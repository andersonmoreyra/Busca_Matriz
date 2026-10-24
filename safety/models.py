from django.db import models
from assets.models import Ativo
from orders.models import OrdemServico
from django.contrib.auth.models import User

class PermissaoTrabalho(models.Model):
    ordem_servico = models.OneToOneField(OrdemServico, on_delete=models.CASCADE, related_name='permissao_trabalho', verbose_name="Ordem de Serviço")
    emitente = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='pts_emitidas', verbose_name="Emitente")

    trabalho_altura = models.BooleanField(default=False, verbose_name="Trabalho em Altura?")
    espaco_confinado = models.BooleanField(default=False, verbose_name="Espaço Confinado?")
    trabalho_quente = models.BooleanField(default=False, verbose_name="Trabalho a Quente?")
    eletricidade = models.BooleanField(default=False, verbose_name="Alta Tensão / Eletricidade?")

    valido_ate = models.DateTimeField(verbose_name="Válido Até (Data e Hora)")
    status = models.CharField(max_length=50, choices=[
        ('solicitada', 'Solicitada'),
        ('aprovada', 'Aprovada / Liberada'),
        ('revogada', 'Revogada / Suspensa'),
        ('encerrada', 'Encerrada')
    ], default='solicitada', verbose_name="Status")

    def __str__(self):
        return f"PT - OS {self.ordem_servico.numero} ({self.get_status_display()})"

    class Meta:
        verbose_name = "Permissão de Trabalho"
        verbose_name_plural = "Permissões de Trabalho"


class IsolamentoLOTO(models.Model):
    permissao = models.ForeignKey(PermissaoTrabalho, on_delete=models.CASCADE, related_name='procedimentos_loto', verbose_name="Permissão de Trabalho")
    ativo = models.ForeignKey(Ativo, on_delete=models.CASCADE, verbose_name="Equipamento Bloqueado")

    ponto_bloqueio = models.CharField(max_length=255, verbose_name="Ponto de Bloqueio (ex: Disjuntor Principal)")
    tipo_energia = models.CharField(max_length=50, choices=[
        ('eletrica', 'Elétrica'),
        ('mecanica', 'Mecânica'),
        ('hidraulica', 'Hidráulica'),
        ('pneumatica', 'Pneumática'),
        ('quimica', 'Química')
    ], verbose_name="Tipo de Energia")

    data_aplicacao = models.DateTimeField(verbose_name="Data/Hora Aplicação do Bloqueio")
    data_remocao = models.DateTimeField(blank=True, null=True, verbose_name="Data/Hora Remoção do Bloqueio")

    aplicado_por = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='bloqueios_aplicados', verbose_name="Bloqueado por")
    removido_por = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name='bloqueios_removidos', verbose_name="Removido por")

    def __str__(self):
        return f"LOTO {self.ponto_bloqueio} - {self.ativo.nome}"

    class Meta:
        verbose_name = "Isolamento LOTO"
        verbose_name_plural = "Isolamentos LOTO"
