from django.db import models
from assets.models import Ativo
from django.contrib.auth.models import User

class SolicitacaoManutencao(models.Model):
    ativo = models.ForeignKey(Ativo, on_delete=models.CASCADE, related_name='solicitacoes', verbose_name="Ativo")
    solicitante = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='solicitacoes_criadas', verbose_name="Solicitante")
    data_solicitacao = models.DateTimeField(auto_now_add=True, verbose_name="Data da Solicitação")
    descricao = models.TextField(verbose_name="Descrição da Falha / Sintoma")

    urgencia = models.CharField(max_length=50, choices=[
        ('baixa', 'Baixa'),
        ('media', 'Média'),
        ('alta', 'Alta'),
        ('emergencia', 'Emergência')
    ], default='media', verbose_name="Urgência")

    status = models.CharField(max_length=50, choices=[
        ('pendente', 'Pendente de Triagem'),
        ('aprovada', 'Aprovada'),
        ('rejeitada', 'Rejeitada'),
        ('convertida', 'Convertida em OS')
    ], default='pendente', verbose_name="Status")

    def __str__(self):
        return f"Solicitação #{self.id} - {self.ativo.nome} ({self.get_status_display()})"

    class Meta:
        verbose_name = "Solicitação de Manutenção"
        verbose_name_plural = "Solicitações de Manutenção"


class OrdemServico(models.Model):
    numero = models.CharField(max_length=50, unique=True, verbose_name="Número da OS")
    solicitacao_origem = models.OneToOneField(SolicitacaoManutencao, on_delete=models.SET_NULL, null=True, blank=True, related_name='ordem_servico', verbose_name="Solicitação de Origem")
    ativo = models.ForeignKey(Ativo, on_delete=models.CASCADE, related_name='ordens_servico', verbose_name="Ativo")
    descricao = models.TextField(verbose_name="Descrição do Serviço")

    tipo_manutencao = models.CharField(max_length=50, choices=[
        ('corretiva', 'Corretiva'),
        ('preventiva', 'Preventiva'),
        ('preditiva', 'Preditiva'),
        ('melhoria', 'Melhoria'),
        ('rotina', 'Rotina')
    ], default='corretiva', verbose_name="Tipo de Manutenção")

    prioridade = models.CharField(max_length=50, choices=[
        ('baixa', 'Baixa'),
        ('media', 'Média'),
        ('alta', 'Alta'),
        ('urgente', 'Urgente')
    ], default='media', verbose_name="Prioridade")

    status = models.CharField(max_length=50, choices=[
        ('aberta', 'Aberta'),
        ('planejamento', 'Em Planejamento'),
        ('execucao', 'Em Execução'),
        ('aguardando', 'Aguardando Material/Aprovação'),
        ('concluida', 'Concluída'),
        ('cancelada', 'Cancelada')
    ], default='aberta', verbose_name="Status")

    data_criacao = models.DateTimeField(auto_now_add=True, verbose_name="Data de Criação")
    data_prevista_inicio = models.DateField(blank=True, null=True, verbose_name="Previsão de Início")
    data_prevista_fim = models.DateField(blank=True, null=True, verbose_name="Previsão de Término")

    responsavel = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name='ordens_responsaveis', verbose_name="Responsável")

    def __str__(self):
        return f"OS {self.numero} - {self.ativo.nome} ({self.get_status_display()})"

    class Meta:
        verbose_name = "Ordem de Serviço"
        verbose_name_plural = "Ordens de Serviço"


class TarefaOS(models.Model):
    ordem_servico = models.ForeignKey(OrdemServico, on_delete=models.CASCADE, related_name='tarefas', verbose_name="Ordem de Serviço")
    descricao = models.CharField(max_length=255, verbose_name="Descrição da Tarefa")
    concluida = models.BooleanField(default=False, verbose_name="Concluída")

    def __str__(self):
        return f"Tarefa: {self.descricao} - OS {self.ordem_servico.numero}"

    class Meta:
        verbose_name = "Tarefa da OS"
        verbose_name_plural = "Tarefas da OS"
