# 📦 SGE — Sistema de Gestão de Estoque

![Python](https://img.shields.io/badge/Python-3776AB?logo=python&logoColor=white)
![Django](https://img.shields.io/badge/Django%204.2-092E20?logo=django&logoColor=white)
![DRF](https://img.shields.io/badge/Django%20REST-A30000?logo=django&logoColor=white)
![JWT](https://img.shields.io/badge/JWT-000000?logo=jsonwebtokens&logoColor=white)

Sistema de **gestão de estoque** feito em **Django**: cadastro de produtos, controle de entradas e saídas, e um **painel de métricas** (custo, venda, lucro e quantidade). Tem **interface web** (com login) e uma **API REST** protegida por **JWT**.

## ✨ Funcionalidades

- **Cadastros:** marcas, fornecedores, categorias e produtos.
- **Movimentação de estoque:** entradas (*inflows*) e saídas (*outflows*) — a saída baixa o estoque do produto.
- **Painel de métricas:** total em custo, total em venda, **lucro** e quantidade total em estoque.
- **Autenticação:** login/logout na web e **JWT** (`djangorestframework-simplejwt`) na API.
- **Admin do Django** para gestão rápida dos dados.

## 🧱 Apps

| App | Responsabilidade |
| --- | --- |
| `brands` | Marcas |
| `suppliers` | Fornecedores |
| `categories` | Categorias |
| `products` | Produtos (preço de custo, preço de venda, quantidade) |
| `inflows` | Entradas de estoque |
| `outflows` | Saídas de estoque |
| `authentication` | Autenticação da API (JWT) |

## 🛠️ Stack

`Python` · `Django 4.2` · `Django REST Framework` · `SimpleJWT` · `SQLite`

## 🚀 Como rodar

```bash
# 1. clonar e entrar na pasta
git clone https://github.com/JRFilho1503/SGE.git
cd SGE

# 2. ambiente virtual
python -m venv venv
source venv/bin/activate        # Windows: venv\Scripts\activate

# 3. dependências
pip install -r requirements.txt

# 4. banco e usuário admin
python manage.py migrate
python manage.py createsuperuser

# 5. subir o servidor
python manage.py runserver
```

Acesse **http://localhost:8000** (web) e **http://localhost:8000/admin** (admin).
A API fica sob **`/api/v1/`** e exige token JWT.

## 🔑 API (JWT)

```bash
# obter token
curl -X POST http://localhost:8000/api/v1/authentication/token/ \
  -d "username=SEU_USER&password=SUA_SENHA"

# usar o token
curl http://localhost:8000/api/v1/... \
  -H "Authorization: Bearer <access_token>"
```

---

Projeto de estudo/prática em Django + DRF. Dúvidas ou sugestões são bem-vindas.
