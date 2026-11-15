# Modelos do sistema de estoque
from django.core.exceptions import ValidationError
from django.db import models


class Categoria(models.Model):
    nome = models.CharField(max_length=80)
    descricao = models.TextField(blank=True)

    def __str__(self):
        return self.nome


class Produto(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.TextField(blank=True)
    preco = models.DecimalField(max_digits=8, decimal_places=2)
    quantidade = models.PositiveIntegerField(default=0)
    data_cadastro = models.DateTimeField(auto_now_add=True)
    # relacionamento: uma categoria tem varios produtos
    # PROTECT = nao deixa apagar a categoria se ainda tiver produto nela
    categoria = models.ForeignKey(Categoria, on_delete=models.PROTECT)

    def __str__(self):
        return self.nome


class Movimentacao(models.Model):
    ENTRADA = "E"
    SAIDA = "S"
    TIPOS = [
        (ENTRADA, "Entrada"),
        (SAIDA, "Saída"),
    ]

    # um produto tem varias movimentacoes
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE)
    tipo = models.CharField(max_length=1, choices=TIPOS)
    quantidade = models.PositiveIntegerField()
    data = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.get_tipo_display()} - {self.produto.nome} ({self.quantidade})"

    # REGRA DE NEGOCIO 1: nao deixa fazer uma saida maior que o estoque.
    # o clean() e chamado automaticamente pelo formulario (e pelo admin)
    def clean(self):
        if self.produto_id and self.tipo == self.SAIDA and self.quantidade:
            if self.quantidade > self.produto.quantidade:
                raise ValidationError(
                    f"Estoque insuficiente! Temos apenas {self.produto.quantidade} "
                    f"unidade(s) de {self.produto.nome}."
                )

    # REGRA DE NEGOCIO 2: depois de salvar a movimentacao, atualiza o estoque
    # do produto sozinho (entrada soma, saida subtrai)
    def save(self, *args, **kwargs):
        # so mexe no estoque quando a movimentacao e nova
        if self.pk is None:
            if self.tipo == self.ENTRADA:
                self.produto.quantidade += self.quantidade
            else:
                self.produto.quantidade -= self.quantidade
            self.produto.save()
        super().save(*args, **kwargs)
