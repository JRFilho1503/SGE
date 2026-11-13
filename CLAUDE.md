# CLAUDE.md — SGE (Sistema de Gestão de Estoque)

Guia para o Claude Code trabalhar neste repositório. Leia antes de editar.

## O que é
Sistema de **gestão de estoque** — Django 4.2 + DRF + SimpleJWT. Tem **interface web** (com login) e **API REST** (JWT). Projeto pessoal de estudo/portfólio de José Roberto (JRFilho1503).

## Apps e domínio
- `brands`, `suppliers`, `categories`, `products` (preço de custo/venda, quantidade).
- `inflows` (entradas) e `outflows` (saídas) — **a saída baixa o estoque do produto** (regra de negócio central).
- Painel de **métricas**: custo total, venda total, lucro e quantidade em estoque.
- `authentication` (JWT da API).

## Stack
Python · Django 4.2 · DRF · djangorestframework-simplejwt · flake8 · SQLite.

## Como rodar
```bash
python -m venv venv && source venv/bin/activate
pip install -r requirements.txt
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

## Convenções
- **Lint:** flake8 (`.flake8`) — rode antes de commitar.
- Padrão Django por app (models/serializers/views/urls/migrations).
- **Atenção à regra de estoque:** toda saída (outflow) deve debitar a quantidade do produto; não quebrar esse invariante.

## Ao adicionar/alterar
- Novo recurso = model + serializer/form + view + url + migration.
- Validar que o saldo de estoque permanece consistente após entradas/saídas.
- Rodar a suíte de testes (quando houver) antes de commitar.

## Não faça
- Não commitar `db.sqlite3` nem segredos (ver `.gitignore`).
- Não permitir saída que deixe o estoque negativo sem tratamento.
