from django.shortcuts import render
from django.http import HttpResponse
from core.models import Comunicado,Categoria


def home(request):
    nivel = request.GET.get('nivel', None)
    categorias = request.GET.get('categoria', None)

    comunicados = Comunicado.objects.all()
    comunicados = Comunicado.objects.order_by('-fecha_emision')
    categoria = Categoria.objects.all()


    if nivel:
        comunicados = comunicados.filter(nivel=nivel)
    if categorias:
        comunicados = comunicados.filter(fkcategoria=categorias)


    data = {
        'comunicados': comunicados,
        'categorias': categoria
    }
    return render(request,'core/home.html',data)
