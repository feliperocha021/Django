# Criar ambiente virtual
``python -m venv .venv``

# Ativar no Git Bash
``source .venv/Scripts/activate``

# Abra o VS Code na pasta do seu projeto.

Pressione Ctrl+Shift+P → digite Python: Select Interpreter.

Escolha o interpretador que aponta para:
``.venv/Scripts/python.exe``

# Instalar o Django
``pip install django``

# Criar o projeto Django
``django-admin startproject config .``

# Criar o app
``mkdir apps``
``cd apps``
``python ../manage.py startapp cursos``

Um app é uma parte modular do seu sistema, responsável por uma funcionalidade específica.

O projeto é o todo (com as configurações globais), e os apps são os blocos que compõem esse projeto.

# Migrations
Criar migração -> ``python manage.py makemigrations``

Rodar migração -> ``python manage.py migrate``

Desfazer migração -> ``python manage.py migrate app_name migration_name``

# Usário para entrar no painel de administração

Criar superuser -> ``python manage.py createsuperuser``

name: admin
senha: 123

# Executar o projeto
``python manage.py runserver``

Entrar no painel de admin -> http://localhost:8000/admin

# Converter para API REST

Em settings.py: Em INSTALLED_APPS, inserir rest_framework

Testar funcionamento (Browser): http://localhost:8000/api-auth/login

Criar serializers para os models

Criar APIViews para os métodos HTTP

Criar arquivos de rotas locais

Configurar as rotas globais do projeto

Testar funcionamento: http://localhost:8000/api/v1/courses
http://localhost:8000/api/v1/evaluations