# Configuracao do Django Admin
from django.contrib import admin

from .models import Categoria, Movimentacao, Produto


@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ("nome", "descricao")
    search_fields = ("nome",)


@admin.register(Produto)
class ProdutoAdmin(admin.ModelAdmin):
    list_display = ("nome", "categoria", "preco", "quantidade")
    list_filter = ("categoria",)
    search_fields = ("nome",)


@admin.register(Movimentacao)
class MovimentacaoAdmin(admin.ModelAdmin):
    list_display = ("produto", "tipo", "quantidade", "data")
    list_filter = ("tipo",)
