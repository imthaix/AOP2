# Rotas do app estoque
from django.urls import path

from . import views

app_name = "estoque"

urlpatterns = [
    # CRUD de produtos
    path("", views.produto_lista, name="produto_lista"),
    path("produtos/novo/", views.produto_criar, name="produto_criar"),
    path("produtos/<int:pk>/editar/", views.produto_editar, name="produto_editar"),
    path("produtos/<int:pk>/excluir/", views.produto_excluir, name="produto_excluir"),

    # movimentacoes (entrada e saida)
    path("movimentacoes/", views.movimentacao_lista, name="movimentacao_lista"),
    path("movimentacoes/nova/", views.movimentacao_criar, name="movimentacao_criar"),
]
