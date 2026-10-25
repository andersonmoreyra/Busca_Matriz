from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_view, name='home'),
    path('solicitacao/nova/', views.nova_solicitacao_view, name='nova_solicitacao'),
]