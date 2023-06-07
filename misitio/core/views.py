from django.shortcuts import render
from django.http import HttpResponse
from core.models import Comunicado


def home(request):
    comunicados = Comunicado.objects.all()
    data = {
        'comunicados': comunicados
    }
    return render(request,'core/home.html',data)