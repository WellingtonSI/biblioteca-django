from rest_framework.test import APITestCase
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