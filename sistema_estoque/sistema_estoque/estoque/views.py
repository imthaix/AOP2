# Views do sistema de estoque
from django.contrib import messages
from django.shortcuts import get_object_or_404, redirect, render

from .forms import MovimentacaoForm, ProdutoForm
from .models import Movimentacao, Produto


# ---------- CRUD de produtos ----------

def produto_lista(request):
    # READ: lista todos os produtos
    produtos = Produto.objects.all().order_by("nome")
    return render(request, "estoque/produto_lista.html", {"produtos": produtos})


def produto_criar(request):
    # CREATE
    if request.method == "POST":
        form = ProdutoForm(request.POST)
        if form.is_valid():  # valida os dados
            form.save()      # salva no banco
            messages.success(request, "Produto cadastrado com sucesso!")
            return redirect("estoque:produto_lista")
    else:
        form = ProdutoForm()
    return render(request, "estoque/produto_form.html",
                  {"form": form, "titulo": "Novo produto"})


def produto_editar(request, pk):
    # UPDATE
    produto = get_object_or_404(Produto, pk=pk)
    if request.method == "POST":
        form = ProdutoForm(request.POST, instance=produto)
        if form.is_valid():
            form.save()
            messages.success(request, "Produto atualizado!")
            return redirect("estoque:produto_lista")
    else:
        form = ProdutoForm(instance=produto)
    return render(request, "estoque/produto_form.html",
                  {"form": form, "titulo": "Editar produto"})


def produto_excluir(request, pk):
    # DELETE: mostra uma tela pedindo confirmacao antes de apagar
    produto = get_object_or_404(Produto, pk=pk)
    if request.method == "POST":
        produto.delete()
        messages.success(request, "Produto excluído.")
        return redirect("estoque:produto_lista")
    return render(request, "estoque/confirmar_exclusao.html", {"produto": produto})


# ---------- movimentacoes ----------

def movimentacao_lista(request):
    movimentacoes = Movimentacao.objects.all().order_by("-data")
    return render(request, "estoque/movimentacao_lista.html",
                  {"movimentacoes": movimentacoes})


def movimentacao_criar(request):
    # formulario -> validacao -> salva (o estoque e atualizado no model) -> mensagem
    if request.method == "POST":
        form = MovimentacaoForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Movimentação registrada e estoque atualizado!")
            return redirect("estoque:movimentacao_lista")
    else:
        form = MovimentacaoForm()
    return render(request, "estoque/movimentacao_form.html", {"form": form})
