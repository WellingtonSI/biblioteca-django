from rest_framework import serializers
from .models import Categoria, Autor, Livro, Colecao
from django.contrib.auth.models import User

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ("url", "pk", "username")
        
class CategoriaSerializer(serializers.HyperlinkedModelSerializer):
    class Meta: 
        model = Categoria
        fields = ['url','id', 'nome']
 
class AutorSerializer(serializers.HyperlinkedModelSerializer):
    class Meta: 
        model = Autor
        fields = ['url','id', 'nome']
    
class LivroSerializer(serializers.HyperlinkedModelSerializer):
    autor = serializers.PrimaryKeyRelatedField(queryset=Autor.objects.all())
    categoria = serializers.PrimaryKeyRelatedField(queryset=Categoria.objects.all())

    class Meta: 
        model = Livro
        fields = ['url','id', 'titulo', 'autor', 'categoria','publicado_em']
        
class ColecaoSerializer(serializers.ModelSerializer):
    livros = serializers.PrimaryKeyRelatedField(many=True, queryset=Livro.objects.all())
    colecionador = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())
    
    class Meta:
        model = Colecao
        fields = ['url','id', 'nome', 'descricao', 'livros', 'colecionador']