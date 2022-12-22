# Escola

Sistema para matricular alunos em cursos implementado em Django Rest API

## Como desenvolver?

1. Clone o repositório
2. Crie um virtualenv com Python 3.11.0
3. Ative o virtualenv
4. Instale as dependências
5. Configure a instância com o .env
6. Execute os testes

```console
git clone git@github.com:felipeabreu86/python-django-rest-api-escola.git
cd python-django-rest-api-escola
python -m venv .venv
./.venv/scripts/activate
pip install -r requirements-dev.txt
cp contrib/env-sample .env
python manage.py test
```