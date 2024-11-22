# Meu Projeto Django Rest Framework

## Descrição

Este é um projeto de exemplo que utiliza o Django Rest Framework (DRF) para criar uma API RESTful simulando sistema de cadastros em biblioteca. O projeto inclui autenticação de usuários, CRUD (Create, Read, Update, Delete) para modelos de exemplo como `Autor`, `Categoria`, `Livro` e `Colecao`.

## Instalação

### 1. Clonar o Repositório

```bash
git clone https://github.com/WellingtonSI/biblioteca-django.git
cd biblioteca
```
### 2. Configurar o Ambiente Virtual

```bash
python -m venv venv
source venv/bin/activate  # No Windows, use `venv\Scripts\activate`
```
### 3. Instalar Dependências
```bash
pip install -r requirements.txt
```

### 4. Configurar o Banco de Dados
Crie um banco de dados PostgreSQL (ou outro banco de dados suportado pelo Django) e configure as credenciais no arquivo settings.py:

```bash
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'seu_banco_de_dados',
        'USER': 'seu_usuario',
        'PASSWORD': 'sua_senha',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
```
### 5. Aplicar Migrações
```bash
python manage.py migrate
```
### 6. Criar um Superusuário
```bash
python manage.py createsuperuser
```
### 7. Executar o Servidor de Desenvolvimento
```bash
python manage.py runserver
```

### Funcionalidades
* Autenticação de Usuários: Utilizando tokens de autenticação.
* CRUD para Modelos: Operações de criação, leitura, atualização e exclusão para modelos como Autor, Categoria, Livro e Colecao.
* Testes Automatizados: Testes unitários e de integração utilizando o framework de testes do Django.
  
### Testes
Para executar os testes, utilize o comando:

```bash
coverage run -m pytest
```