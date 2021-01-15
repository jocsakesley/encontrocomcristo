# encontrocomcristo
Projeto destinado a gestão de ECC e EJC de igrejas evangélicas.


## Este projeto foi feito com:

* [Python 3](https://www.python.org/)
* [Django 3.1.2](https://www.djangoproject.com/)
* Django Rest Framework 3.12.2

## Como rodar o projeto?

* Clone esse repositório.
* Crie um virtualenv com Python 3.
* Ative o virtualenv.
* Instale as dependências.
* Rode as migrações.

```
git clone https://github.com/dioney/encontrocomcristo.git
cd encontrocomcristo
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python contrib/env_gen.py
python manage.py migrate
```