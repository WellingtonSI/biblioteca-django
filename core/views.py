from django.views.decorators.csrf import csrf_exempt
from rest_framework.response import Response
from rest_framework import status
from .models import Livro, Autor, Categoria
from .serializers import LivroSerializer, AutorSerializer, CategoriaSerializer
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from django.http import HttpResponse

class JSONResponse(HttpResponse):
    def __init__(self,data,**kwargs):
        content = JSONRenderer().render(data)
        kwargs['content_type'] = 'application/json'
        super(JSONResponse, self).__init__(content, **kwargs)

@csrf_exempt
def livro_list_create(request):
    if request.method == 'GET':
        livros = Livro.objects.all()
        serializer = LivroSerializer(livros, many=True)
        return JSONResponse(serializer.data)
    
    if request.method == 'POST':
        livro_data = JSONParser().parse(request)
        serializer = LivroSerializer(data = livro_data)
        if serializer.is_valid():
            serializer.save()
            return JSONResponse(serializer.data, status=status.HTTP_201_CREATED)
        return JSONResponse(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
  
@csrf_exempt 
def livro_detail(request, pk):
    livro = Livro.objects.get(pk=pk)
    
    if request.method == 'GET':
        serializer = LivroSerializer(livro)
        return JSONResponse(serializer.data)
    
    if request.method == 'PUT':
        livro_data = JSONParser().parse(request)
        serializer = LivroSerializer(livro, data = livro_data)
        if serializer.is_valid():
            serializer.save()
            return JSONResponse(serializer.data)
        return JSONResponse(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
    if request.method == 'DELETE':
        livro.delete()
        return HttpResponse(status = status.HTTP_204_NO_CONTENT)
    
@csrf_exempt
def autor_list_create(request):
    if request.method == 'GET':
        autores = Autor.objects.all()
        serializer = AutorSerializer(autores, many=True)
        return JSONResponse(serializer.data)
    
    if request.method == 'POST':
        autor_data = JSONParser().parse(request)
        serializer = AutorSerializer(data = autor_data)
        if serializer.is_valid():
            serializer.save()
            return JSONResponse(serializer.data, status=status.HTTP_201_CREATED)
        return JSONResponse(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
  
@csrf_exempt 
def autor_detail(request, pk):
    autor = Autor.objects.get(pk=pk)
    
    if request.method == 'GET':
        serializer = AutorSerializer(autor)
        return JSONResponse(serializer.data)
    
    if request.method == 'PUT':
        autor_data = JSONParser().parse(request)
        serializer = AutorSerializer(autor, data = autor_data)
        if serializer.is_valid():
            serializer.save()
            return JSONResponse(serializer.data)
        return JSONResponse(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
    if request.method == 'DELETE':
        autor.delete()
        return HttpResponse(status = status.HTTP_204_NO_CONTENT)
    
@csrf_exempt
def categoria_list_create(request):
    if request.method == 'GET':
        categoria = Categoria.objects.all()
        serializer = CategoriaSerializer(categoria, many=True)
        return JSONResponse(serializer.data)
    
    if request.method == 'POST':
        categoria_data = JSONParser().parse(request)
        serializer = CategoriaSerializer(data = categoria_data)
        if serializer.is_valid():
            serializer.save()
            return JSONResponse(serializer.data, status=status.HTTP_201_CREATED)
        return JSONResponse(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
  
@csrf_exempt 
def categoria_detail(request, pk):
    categoria = Categoria.objects.get(pk=pk)
    
    if request.method == 'GET':
        serializer = CategoriaSerializer(categoria)
        return JSONResponse(serializer.data)
    
    if request.method == 'PUT':
        categoria_data = JSONParser().parse(request)
        serializer = CategoriaSerializer(categoria, data = categoria_data)
        if serializer.is_valid():
            serializer.save()
            return JSONResponse(serializer.data)
        return JSONResponse(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
    if request.method == 'DELETE':
        categoria.delete()
        return HttpResponse(status = status.HTTP_204_NO_CONTENT)