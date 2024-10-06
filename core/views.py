from rest_framework import generics
from .models import Livro, Autor, Categoria
from .serializers import LivroSerializer, AutorSerializer, CategoriaSerializer



class LivroList(generics.ListCreateAPIView):
    queryset = Livro.objects.all()
    serializer_class = LivroSerializer
    name = "livro-list"
  
class LivroDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Livro.objects.all()
    serializer_class = LivroSerializer
    name = "livro-detail"
    
class AutorList(generics.ListCreateAPIView):
    queryset = Autor.objects.all()
    serializer_class = AutorSerializer
    name = "autor-list"
    
class AutorDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Autor.objects.all()
    serializer_class = AutorSerializer
    name = "autor-detail"

class CategoriaList(generics.ListCreateAPIView):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer
    name = "categoria-list"

class CategoriaDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer
    name = "categoria-detail"