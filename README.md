<h1 align="center">
    <img alt="Encurtador de URLs" title="Encurtador de URLs" src="setup/static/images/django.svg" width="50px" />
</h1>

<h4 align="center">
  	Encurtador de URLs (BACKEND)
</h4>

<p align="center">
	<a href="#-tecnologias">Tecnologias</a>&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;
	<a href="#-projeto">Projeto</a>&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;
	<a href="#instalação">Instalação</a>
</p>

## 🤖 Tecnologias

Esse projeto está sendo desenvolvido com as seguintes tecnologias:

- [Django](https://www.djangoproject.com/)
- [Django-Rest-Framework](https://www.django-rest-framework.org/)
- [Django REST framework JWT](https://jpadilla.github.io/django-rest-framework-jwt)


## 💻 Projeto
**API para salvar e encurtar URLs**

## Instalação

### Pré requisitos
Ter instalado:
- [Python](https://www.python.org/downloads/)

### Clonar repositórios
```sh
# Clonar repositório do backend
git clone https://github.com/andre23arruda/django-shortener-url.git

# Clonar repositório do frontend
git clone https://github.com/andre23arruda/create-react-app-lambda.git
```


### Renomear arquivo com variáveis de ambiente
-  **Renomear _backend/setup/env_example.py_ para _backend/setup/env.py_**

### No terminal, rodar
```sh
# Entrar na pasta dos arquivos do backend
cd backend

# Criar um ambiente virtual
python -m venv venv

# Ativar o ambiente virtual
. venv/Scripts/activate
# ou (em linux)
. venv/bin/activate

# Instalar os pacotes necessários
pip install -r requirements.txt

# Executar as migrações
python manage.py migrate

# Criar superusuário (poderá fazer login e entrar no admin)
echo "from django.contrib.auth.models import User; User.objects.create_superuser('teste', 'teste@example.com', 'teste1234')" | python manage.py shell
# username -> teste
# password -> teste1234

# Run
python manage.py runserver
```
