# Formularios do sistema
from django import forms

from .models import Movimentacao, Produto


class ProdutoForm(forms.ModelForm):
    class Meta:
        model = Produto
        fields = ["nome", "descricao", "categoria", "preco", "quantidade"]


class MovimentacaoForm(forms.ModelForm):
    class Meta:
        model = Movimentacao
        fields = ["produto", "tipo", "quantidade"]

    # validacao: a quantidade precisa ser maior que zero
    def clean_quantidade(self):
        quantidade = self.cleaned_data["quantidade"]
        if quantidade <= 0:
            raise forms.ValidationError("A quantidade deve ser maior que zero.")
        return quantidade
