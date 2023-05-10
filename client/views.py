from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from .form import ClientForm, PostForm, HistoryForm
from django.views.generic.edit import CreateView
from .models import *
from django.views.generic import ListView

# def client(request):
#     return render(request, template_name="client/client.html")


class PatientCreateView(CreateView):
    model = Client
    form_class = ClientForm
    success_url = reverse_lazy('otvet')
    template_name = "client_form.html"
    context_object_name = 'form'



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




class HistoryCreateView(CreateView):
    model = History
    form_class = HistoryForm
    success_url = reverse_lazy('history')
    template_name = "client/history_form.html"
    context_object_name = 'his'

def HistoryListView(request): 
    history = History.objects.all()
    if request.method=='POST':
        search =request.POST['question']
        g = []
        for i in history:
            l = i.patient
            if str(l).count(str(search)) > 0:
                g.append(i)
        history = g
    return render(request,'client/history.html',{'object_list':history})






def history_info(request, pk):
    his_info = History.objects.all().filter(id = pk)

    return render(request, 'client/history_list.html', {'h': his_info})
