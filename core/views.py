from rest_framework import generics
from .models import Livro, Autor, Categoria, Colecao
from .serializers import LivroSerializer, AutorSerializer, CategoriaSerializer, ColecaoSerializer
from core.filters import LivroFilter,CategoriaFilter,AutorFilter
from rest_framework import permissions
from core import custom_permissions
from rest_framework.authentication import TokenAuthentication
from rest_framework.response import Response
from rest_framework.reverse import reverse


class ApiRoot(generics.GenericAPIView):
    name = "api-root"

    def get(self, request, *args, **kwargs):
        return Response(
            {
                "livros": reverse(LivroList.name, request=request),
                "autores": reverse(AutorList.name, request=request),
                "categorias": reverse(CategoriaList.name, request=request),
                "colecoes": reverse(ColecaoListCreate.name, request=request),
            }
        )
        
class LivroList(generics.ListCreateAPIView):
    queryset = Livro.objects.all()
    name='livros-list'
    serializer_class = LivroSerializer
    filterset_class = LivroFilter
    ordering_fields = ('titulo', 'autor', 'categoria', 'publicado_em')
    
class LivroDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Livro.objects.all()
    name='livro-detail'
    serializer_class = LivroSerializer
    
class AutorList(generics.ListCreateAPIView):
    queryset = Autor.objects.all()
    name='autores-list'
    serializer_class = AutorSerializer
    filterset_class = AutorFilter
    ordering_fields = ('nome',)
    
class AutorDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Autor.objects.all()
    serializer_class = AutorSerializer
    name = "autor-detail"

class CategoriaList(generics.ListCreateAPIView):
    queryset = Categoria.objects.all()
    name='categorias-list'
    serializer_class = CategoriaSerializer
    filterset_class = CategoriaFilter
    ordering_fields = ('nome',)

class CategoriaDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Categoria.objects.all()
    name='categoria-detail'
    serializer_class = CategoriaSerializer
    
class ColecaoListCreate(generics.ListCreateAPIView):
    queryset = Colecao.objects.all()
    name='colecao-list-create'
    serializer_class = ColecaoSerializer
    permission_classes = (permissions.IsAuthenticated, custom_permissions.IsCurrentUserOwnerOrReadOnly)
    authentication_classes = (TokenAuthentication,)

    def perform_create(self, serializer):
        serializer.save(colecionador=self.request.user)

class ColecaoDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Colecao.objects.all()
    name='colecao-detail'
    serializer_class = ColecaoSerializer
    permission_classes = (permissions.IsAuthenticated, custom_permissions.IsCurrentUserOwnerOrReadOnly)
    authentication_classes = (TokenAuthentication,)