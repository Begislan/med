from django.shortcuts import render
from articles.models import *

from articles.models import Article
from client.models import Departament, Doctor


# Create your views here.
def index(request):
    article = Article.objects.all()
    context = {
        'article': article
    }

    return render(request, "front/index.html", context)




def dep(request):
    info = Departament.objects.all()
    context = {
        'info': info,
    }
    return render(request, 'front/depertament.html', context)


def dep_view(request, pk):
    info = Departament.objects.all().filter(id = pk)
    inf = Departament.objects.all().filter(id=pk)
    doctor = Doctor.objects.all().filter(id=pk)
    context = {
        'inf': inf,
        'info': info,
        'doc': doctor,
    }
    return render(request, 'front/about.html', context)

def onas(request):
    return render(request, "front/onas.html")

