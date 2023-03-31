from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from .form import ClientForm, PostForm
from django.views.generic.edit import CreateView
from .models import *
from django.http import HttpResponseRedirect
from django.views.generic import ListView

# def client(request):
#     return render(request, template_name="client/client.html")

def client_form(request):
    form = ClientForm()
    context = {
        'form': form
    }
    return render(request, 'client_form.html', context)


class BlogCreateView(CreateView):
    model = Client
    form_class = ClientForm
    success_url = reverse_lazy('otvet')
    template_name = "client_form.html"
    
def otvet(request):
    return render(request, "otvet.html")

def doctor(request):
    jav = Client.objects.all().order_by('id')
    return render(request, "doctor/doctor.html", {'jav': jav})


class BlogListView(ListView):
    model = Post
    template_name = 'client/client.html'
    context_object_name = 'posts'

def index(request):

    form = None
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('thanks')
    else:

        form = PostForm()
    return render(request, 'index.html',{'form':form})
    
def thanks(request):
    return render(request, "thanks.html")


def DepartementViews(request):

    info = Departament.objects.all()
    doctor = Doctor.objects.all()
    context = {
        'info': info,
        'doc': doctor,
    }
    return render(request, 'info/info.html', context)



def det_view(request, pk):
    info = Departament.objects.all().filter(id = pk)
    inf = Departament.objects.all().filter(id=pk)
    doctor = Doctor.objects.all().filter(id=pk)
    context = {
        'inf': inf,
        'info': info,
        'doc': doctor,
    }
    return render(request, 'info/info_det.html', context)