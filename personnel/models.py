from django.db import models
from django.contrib.auth.models import User
from orders.models import OrdemServico

class Especialidade(models.Model):
    nome = models.CharField(max_length=100, unique=True, verbose_name="Especialidade (ex: Mecânico, Eletricista)")
    descricao = models.TextField(blank=True, null=True, verbose_name="Descrição")

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name = "Especialidade"
        verbose_name_plural = "Especialidades"


class Equipe(models.Model):
    nome = models.CharField(max_length=100, unique=True, verbose_name="Nome da Equipe")
    supervisor = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name='equipes_supervisionadas', verbose_name="Supervisor")

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name = "Equipe"
        verbose_name_plural = "Equipes"


class Funcionario(models.Model):
    usuario = models.OneToOneField(User, on_delete=models.CASCADE, related_name='perfil_funcionario', verbose_name="Usuário do Sistema")
    matricula = models.CharField(max_length=50, unique=True, verbose_name="Matrícula")
    equipe = models.ForeignKey(Equipe, on_delete=models.SET_NULL, null=True, blank=True, related_name='membros', verbose_name="Equipe")
    especialidade = models.ForeignKey(Especialidade, on_delete=models.SET_NULL, null=True, blank=True, verbose_name="Especialidade Principal")
    valor_hora = models.DecimalField(max_digits=8, decimal_places=2, default=0.00, verbose_name="Custo por Hora")

    def __str__(self):
        return f"{self.usuario.get_full_name() or self.usuario.username} - {self.matricula}"

    class Meta:
        verbose_name = "Funcionário"
        verbose_name_plural = "Funcionários"


class ApontamentoHoras(models.Model):
    ordem_servico = models.ForeignKey(OrdemServico, on_delete=models.CASCADE, related_name='apontamentos', verbose_name="Ordem de Serviço")
    funcionario = models.ForeignKey(Funcionario, on_delete=models.CASCADE, related_name='apontamentos', verbose_name="Funcionário")

    data_trabalho = models.DateField(verbose_name="Data")
    hora_inicio = models.TimeField(verbose_name="Hora Início")
    hora_fim = models.TimeField(verbose_name="Hora Fim")

    descricao = models.TextField(blank=True, null=True, verbose_name="Descrição do Trabalho Realizado")

    def __str__(self):
        return f"Apontamento de {self.funcionario.usuario.username} na OS {self.ordem_servico.numero}"

    class Meta:
        verbose_name = "Apontamento de Hora"
        verbose_name_plural = "Apontamentos de Horas"
