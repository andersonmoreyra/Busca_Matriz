from django.shortcuts import render, redirect
from orders.models import SolicitacaoManutencao, OrdemServico
from assets.models import Ativo

def home_view(request):
    # Estatísticas básicas para o dashboard público
    total_ativos = Ativo.objects.count()
    solicitacoes_pendentes = SolicitacaoManutencao.objects.filter(status='pendente').count()
    os_abertas = OrdemServico.objects.exclude(status__in=['concluida', 'cancelada']).count()

    context = {
        'total_ativos': total_ativos,
        'solicitacoes_pendentes': solicitacoes_pendentes,
        'os_abertas': os_abertas,
    }
    return render(request, 'core_web/home.html', context)

def nova_solicitacao_view(request):
    if request.method == 'POST':
        ativo_id = request.POST.get('ativo')
        descricao = request.POST.get('descricao')
        urgencia = request.POST.get('urgencia')

        ativo = Ativo.objects.get(id=ativo_id)

        SolicitacaoManutencao.objects.create(
            ativo=ativo,
            descricao=descricao,
            urgencia=urgencia,
        )
        return redirect('home')

    ativos = Ativo.objects.all()
    return render(request, 'core_web/solicitacao.html', {'ativos': ativos})