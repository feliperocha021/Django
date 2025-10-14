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

# Relações

ForeignKey -> cria uma relação muitos-para-um.

OneToOneField -> cria uma relação um-para-um.

ManyToManyField -> cria uma relação N-N.

# Paginação

O **Django REST Framework (DRF)** oferece suporte nativo à paginação de resultados.  
Existem duas formas principais de configurar: **global** e **local**.

## 🔹 Paginação Global
Definida no `settings.py`, afeta **toda a API**.

*settings.py*
``` bash
REST_FRAMEWORK = {
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
    'PAGE_SIZE': 10,   # número de itens por página
}
```

É simples e consistente em toda a API, porém menos flexível se endpoints diferentes precisarem de paginações distintas

## Paginação Local
Definida diretamente em um **ViewSet** ou **APIView**. Sobrescreve a configuração global apenas para aquele recurso.

from rest_framework.pagination import PageNumberPagination

``` bash
class CoursePagination(PageNumberPagination):
    page_size = 5
    page_size_query_param = 'page_size'  # permite o cliente escolher
    max_page_size = 50

class CourseViewSet(viewsets.ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    pagination_class = CoursePagination
```

É flexível, cada recurso pode ter sua própria paginação, porém mais código para manter
