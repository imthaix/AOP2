# Sistema de Controle de Estoque

## Identificação
- **Nome da aplicação:** Sistema de Controle de Estoque
- **Aluna:** (colocar o nome aqui)
- **Disciplina:** Técnicas Avançadas de Programação Web
- **Descrição resumida:** aplicação web feita com Django para cadastrar produtos e controlar as entradas e saídas do estoque.

## Sobre o projeto

**Problema que resolve:** muitas lojas pequenas controlam o estoque no caderno ou em planilha, e isso causa erro no saldo e venda de produto que já acabou.

**Objetivo:** manter o estoque dos produtos organizado e sempre atualizado a cada entrada ou saída.

**Principais funcionalidades:**
- cadastro, listagem, edição e exclusão de produtos (CRUD);
- registro de movimentações de entrada e saída;
- histórico de movimentações;
- categorias e demais cadastros pelo Django Admin.

## Regras de negócio
1. **Saída não pode ser maior que o estoque:** se o usuário tentar tirar mais unidades do que existem, o sistema mostra o erro "Estoque insuficiente" e não registra a movimentação (`Movimentacao.clean()` em `models.py`).
2. **Atualização automática do estoque:** ao registrar uma entrada a quantidade do produto aumenta, e ao registrar uma saída ela diminui (`Movimentacao.save()` em `models.py`).

## Modelos
- `Categoria`
- `Produto` (relacionado a `Categoria` por ForeignKey)
- `Movimentacao` (relacionada a `Produto` por ForeignKey)

## Como executar
```
python -m venv .venv
.venv\Scripts\activate        (no Linux/Mac: source .venv/bin/activate)
pip install -r requirements.txt
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```
Sistema: http://127.0.0.1:8000/
Admin: http://127.0.0.1:8000/admin/

Obs.: as categorias são cadastradas pelo Admin. É preciso ter pelo menos uma categoria antes de cadastrar produtos.

## Tecnologias
Python, Django e SQLite.
