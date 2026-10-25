from django.test import TestCase
from django.urls import reverse
from assets.models import Ativo
from orders.models import SolicitacaoManutencao

class CoreWebTests(TestCase):
    def setUp(self):
        self.ativo = Ativo.objects.create(nome="Máquina de Teste", codigo_patrimonio="MT-001")

    def test_home_view_status_code(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'core_web/home.html')

    def test_nova_solicitacao_view_get(self):
        response = self.client.get(reverse('nova_solicitacao'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'core_web/solicitacao.html')

    def test_nova_solicitacao_post(self):
        response = self.client.post(reverse('nova_solicitacao'), {
            'ativo': self.ativo.id,
            'urgencia': 'alta',
            'descricao': 'Máquina com ruído forte'
        })
        self.assertRedirects(response, reverse('home'))

        # Verify db was updated
        self.assertEqual(SolicitacaoManutencao.objects.count(), 1)
        solicitacao = SolicitacaoManutencao.objects.first()
        self.assertEqual(solicitacao.ativo, self.ativo)
        self.assertEqual(solicitacao.urgencia, 'alta')
        self.assertEqual(solicitacao.descricao, 'Máquina com ruído forte')
