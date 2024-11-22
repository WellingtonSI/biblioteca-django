from rest_framework.test import APITestCase, APIClient
from rest_framework import status
from django.urls import reverse
from .models import Livro, Autor, Categoria, Colecao
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token

class LivroTests(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.token = Token.objects.create(user=self.user)
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)

    def post_livro(self, titulo, autor, categoria, publicado_em):
        url = reverse('livros-list')
        data = {
            "titulo": titulo,
            "autor": autor.id,
            "categoria": categoria.id,
            "publicado_em": publicado_em
        }
        response = self.client.post(url, data, format="json")
        return response

    def test_post_and_get_livro(self):
        autor = Autor.objects.create(nome="Autor Teste")
        categoria = Categoria.objects.create(nome="Categoria Teste")
        new_livro_titulo = "Livro Teste"
        response = self.post_livro(new_livro_titulo, autor, categoria, "2023-01-01")
        self.assertEqual(status.HTTP_201_CREATED, response.status_code)
        self.assertEqual(1, Livro.objects.count())
        self.assertEqual(new_livro_titulo, Livro.objects.get().titulo)

    def test_get_livros_collection(self):
        autor = Autor.objects.create(nome="Autor Teste")
        categoria = Categoria.objects.create(nome="Categoria Teste")
        new_livro_titulo = "Livro Teste"
        self.post_livro(new_livro_titulo, autor, categoria, "2023-01-01")
        url = reverse('livros-list')
        response = self.client.get(url, format="json")
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertEqual(1, response.data["count"])
        self.assertEqual(new_livro_titulo, response.data["results"][0]["titulo"])

    def test_update_livro(self):
        autor = Autor.objects.create(nome="Autor Teste")
        categoria = Categoria.objects.create(nome="Categoria Teste")
        livro_titulo = "Livro Teste"
        response = self.post_livro(livro_titulo, autor, categoria, "2023-01-01")
        url = reverse('livro-detail', args=[response.data["id"]])
        updated_livro_titulo = "Livro Atualizado"
        data = {"titulo": updated_livro_titulo}
        patch_response = self.client.patch(url, data, format="json")
        self.assertEqual(status.HTTP_200_OK, patch_response.status_code)
        self.assertEqual(updated_livro_titulo, patch_response.data["titulo"])

    def test_get_livro(self):
        autor = Autor.objects.create(nome="Autor Teste")
        categoria = Categoria.objects.create(nome="Categoria Teste")
        livro_titulo = "Livro Teste"
        response = self.post_livro(livro_titulo, autor, categoria, "2023-01-01")
        url = reverse('livro-detail', args=[response.data["id"]])
        get_response = self.client.get(url, format="json")
        self.assertEqual(status.HTTP_200_OK, get_response.status_code)
        self.assertEqual(livro_titulo, get_response.data["titulo"])
        
    def test_delete_livro(self):
        autor = Autor.objects.create(nome="Autor Teste")
        categoria = Categoria.objects.create(nome="Categoria Teste")
        livro_titulo = "Livro Teste"
        response = self.post_livro(livro_titulo, autor, categoria, "2023-01-01")
        url = reverse('livro-detail', args=[response.data["id"]])
        delete_response = self.client.delete(url, format="json")
        self.assertEqual(status.HTTP_204_NO_CONTENT, delete_response.status_code)

        get_response = self.client.get(url, format="json")
        self.assertEqual(status.HTTP_404_NOT_FOUND, get_response.status_code)
        
class AutorTests(APITestCase):
    def post_autor(self, nome):
        url = reverse('autores-list')
        data = {"nome": nome}
        response = self.client.post(url, data, format="json")
        return response

    def test_post_and_get_autor(self):
        new_autor_nome = "Autor Teste"
        response = self.post_autor(new_autor_nome)
        self.assertEqual(status.HTTP_201_CREATED, response.status_code)
        self.assertEqual(1, Autor.objects.count())
        self.assertEqual(new_autor_nome, Autor.objects.get().nome)

    def test_get_autores_collection(self):
        new_autor_nome = "Autor Teste"
        self.post_autor(new_autor_nome)
        url = reverse('autores-list')
        response = self.client.get(url, format="json")
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertEqual(1, response.data["count"])
        self.assertEqual(new_autor_nome, response.data["results"][0]["nome"])

    def test_update_autor(self):
        autor_nome = "Autor Teste"
        response = self.post_autor(autor_nome)
        url = reverse('autor-detail', args=[response.data["id"]])
        updated_autor_nome = "Autor Atualizado"
        data = {"nome": updated_autor_nome}
        patch_response = self.client.patch(url, data, format="json")
        self.assertEqual(status.HTTP_200_OK, patch_response.status_code)
        self.assertEqual(updated_autor_nome, patch_response.data["nome"])

    def test_get_autor(self):
        autor_nome = "Autor Teste"
        response = self.post_autor(autor_nome)
        url = reverse('autor-detail', args=[response.data["id"]])
        get_response = self.client.get(url, format="json")
        self.assertEqual(status.HTTP_200_OK, get_response.status_code)
        self.assertEqual(autor_nome, get_response.data["nome"])
        
    def test_delete_categoria(self):
        autor_nome = "Autor Teste"
        response = self.post_autor(autor_nome)
        url = reverse('autor-detail', args=[response.data["id"]])
        delete_response = self.client.delete(url, format="json")
        self.assertEqual(status.HTTP_204_NO_CONTENT, delete_response.status_code)

        get_response = self.client.get(url, format="json")
        self.assertEqual(status.HTTP_404_NOT_FOUND, get_response.status_code)
        
class CategoriaTests(APITestCase):
    def post_categoria(self, nome):
        url = reverse('categorias-list')
        data = {"nome": nome}
        response = self.client.post(url, data, format="json")
        return response

    def test_post_and_get_categoria(self):
        new_categoria_nome = "Categoria Teste"
        response = self.post_categoria(new_categoria_nome)
        self.assertEqual(status.HTTP_201_CREATED, response.status_code)
        self.assertEqual(1, Categoria.objects.count())
        self.assertEqual(new_categoria_nome, Categoria.objects.get().nome)

    def test_get_categorias_collection(self):
        new_categoria_nome = "Categoria Teste"
        self.post_categoria(new_categoria_nome)
        url = reverse('categorias-list')
        response = self.client.get(url, format="json")
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertEqual(1, response.data["count"])
        self.assertEqual(new_categoria_nome, response.data["results"][0]["nome"])

    def test_update_categoria(self):
        categoria_nome = "Categoria Teste"
        response = self.post_categoria(categoria_nome)
        url = reverse('categoria-detail', args=[response.data["id"]])
        updated_categoria_nome = "Categoria Atualizada"
        data = {"nome": updated_categoria_nome}
        patch_response = self.client.patch(url, data, format="json")
        self.assertEqual(status.HTTP_200_OK, patch_response.status_code)
        self.assertEqual(updated_categoria_nome, patch_response.data["nome"])

    def test_get_categoria(self):
        categoria_nome = "Categoria Teste"
        response = self.post_categoria(categoria_nome)
        url = reverse('categoria-detail', args=[response.data["id"]])
        get_response = self.client.get(url, format="json")
        self.assertEqual(status.HTTP_200_OK, get_response.status_code)
        self.assertEqual(categoria_nome, get_response.data["nome"])
        
    def test_delete_categoria(self):
        categoria_nome = "Categoria Teste"
        response = self.post_categoria(categoria_nome)
        url = reverse('categoria-detail', args=[response.data["id"]])

        delete_response = self.client.delete(url, format="json")
        self.assertEqual(status.HTTP_204_NO_CONTENT, delete_response.status_code)

        get_response = self.client.get(url, format="json")
        self.assertEqual(status.HTTP_404_NOT_FOUND, get_response.status_code)

class ColecaoTests(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.token = Token.objects.create(user=self.user)
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)

    def post_livros(self):
        autor = Autor.objects.create(nome="Autor Teste")
        categoria = Categoria.objects.create(nome="Categoria Teste")
        livro1 = Livro.objects.create(titulo="Livro 1", autor=autor, categoria=categoria, publicado_em="2023-01-01")
        livro2 = Livro.objects.create(titulo="Livro 2", autor=autor, categoria=categoria, publicado_em="2023-02-01")
        return [livro1.id,livro2.id]
        
    def post_colecao(self, nome, descricao, livros):
        url = reverse('colecao-list-create')
        data = {
            "nome": nome,
            "descricao": descricao,
            "livros": livros,
            "colecionador": self.user.id
        }
        response = self.client.post(url, data, format="json")
        return response

    def test_post_and_get_colecao(self):
        livroIDs = self.post_livros()
        new_colecao_nome = "Coleção Teste"
        response = self.post_colecao(new_colecao_nome, "Descrição da coleção", livroIDs)
        self.assertEqual(status.HTTP_201_CREATED, response.status_code)
        self.assertEqual(1, Colecao.objects.count())
        self.assertEqual(new_colecao_nome, Colecao.objects.get().nome)
        self.assertEqual(self.user.id, Colecao.objects.get().id)

    def test_get_colecoes_collection(self):
        livroIDs = self.post_livros()
        new_colecao_nome = "Coleção Teste"
        self.post_colecao(new_colecao_nome, "Descrição da coleção", livroIDs)
        url = reverse('colecao-list-create')
        response = self.client.get(url, format="json")
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertEqual(1, response.data["count"])
        self.assertEqual(new_colecao_nome, response.data["results"][0]["nome"])

    def test_update_colecao(self):
        livroIDs = self.post_livros()
        colecao_nome = "Coleção Teste"
        response = self.post_colecao(colecao_nome, "Descrição da coleção", livroIDs)
        url = reverse('colecao-detail', args=[response.data["id"]])
        updated_colecao_nome = "Coleção Atualizada"
        data = {"nome": updated_colecao_nome}
        patch_response = self.client.patch(url, data, format="json")
        self.assertEqual(status.HTTP_200_OK, patch_response.status_code)
        self.assertEqual(updated_colecao_nome, patch_response.data["nome"])

    def test_get_colecao(self):
        livroIDs = self.post_livros()
        colecao_nome = "Coleção Teste"
        response = self.post_colecao(colecao_nome, "Descrição da coleção", livroIDs)
        url = reverse('colecao-detail', args=[response.data["id"]])
        get_response = self.client.get(url, format="json")
        self.assertEqual(status.HTTP_200_OK, get_response.status_code)
        self.assertEqual(colecao_nome, get_response.data["nome"])
    
    def test_delete_colecao(self):
        livroIDs = self.post_livros()
        new_colecao_nome = "Coleção Teste"
        post_response = self.post_colecao(new_colecao_nome, "Descrição da coleção", livroIDs)
        url = reverse('colecao-detail' ,args=[post_response.data["id"]])
        delete_response = self.client.delete(url, format="json")
        self.assertEqual(status.HTTP_204_NO_CONTENT, delete_response.status_code)
        get_response = self.client.get(url, format="json")
        self.assertEqual(status.HTTP_404_NOT_FOUND, get_response.status_code)
    
    def test_get_colecoes_collection_unauthorized(self):
        self.client.credentials()
        url = reverse('colecao-list-create')
        response = self.client.get(url, format="json")
        self.assertEqual(status.HTTP_401_UNAUTHORIZED, response.status_code)
        
    def test_post_and_get_colecao_unauthorized(self):
        livroIDs = self.post_livros()
        new_colecao_nome = "Coleção Teste"
        self.client.credentials()
        response = self.post_colecao(new_colecao_nome, "Descrição da coleção", livroIDs)
        self.assertEqual(status.HTTP_401_UNAUTHORIZED, response.status_code)
        
    def test_get_colecoes_collection_unauthorized(self):
        livroIDs = self.post_livros()
        new_colecao_nome = "Coleção Teste"
        self.post_colecao(new_colecao_nome, "Descrição da coleção", livroIDs)
        self.client.credentials()
        url = reverse('colecao-list-create')
        response = self.client.get(url, format="json")
        self.assertEqual(status.HTTP_401_UNAUTHORIZED, response.status_code)

    def test_update_colecao_unauthorized(self):
        livroIDs = self.post_livros()
        colecao_nome = "Coleção Teste"
        response = self.post_colecao(colecao_nome, "Descrição da coleção", livroIDs)
        self.client.credentials()
        url = reverse('colecao-detail', args=[response.data["id"]])
        updated_colecao_nome = "Coleção Atualizada"
        data = {"nome": updated_colecao_nome}
        patch_response = self.client.patch(url, data, format="json")
        self.assertEqual(status.HTTP_401_UNAUTHORIZED, patch_response.status_code)
        
    def test_delete_colecao_unauthorized(self):
        livroIDs = self.post_livros()
        new_colecao_nome = "Coleção Teste"
        post_response = self.post_colecao(new_colecao_nome, "Descrição da coleção", livroIDs)
        self.client.credentials()
        url = reverse('colecao-detail' ,args=[post_response.data["id"]])
        delete_response = self.client.delete(url, format="json")
        self.assertEqual(status.HTTP_401_UNAUTHORIZED, delete_response.status_code)
        
    def test_user_authorization_update_colecao(self):
        livroIDs = self.post_livros()
        colecao_nome = "Coleção Teste"
        response = self.post_colecao(colecao_nome, "Descrição da coleção", livroIDs)
        url = reverse('colecao-detail', args=[response.data["id"]])
        updated_colecao_nome = "Coleção Atualizada"
        data = {"nome": updated_colecao_nome}
       
        # Modifica as credenciais para um usuário diferente
        self.user = User.objects.create_user(username='testuser1', password='testpassword')
        self.token = Token.objects.create(user=self.user)
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)

        patch_response = self.client.patch(url, data, format="json")
        
        self.assertEqual(status.HTTP_403_FORBIDDEN, patch_response.status_code)


    def test_user_authorization_delete_colecao(self):
        livroIDs = self.post_livros()
        new_colecao_nome = "Coleção Teste"
        post_response = self.post_colecao(new_colecao_nome, "Descrição da coleção", livroIDs)
  
        # Modifica as credenciais para um usuário diferente
        self.user = User.objects.create_user(username='testuser1', password='testpassword')
        self.token = Token.objects.create(user=self.user)
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)
        
        url = reverse('colecao-detail', args=[post_response.data["id"]])
        response = self.client.delete(url, format="json")
        self.assertEqual(status.HTTP_403_FORBIDDEN, response.status_code)