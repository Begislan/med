from django.urls import path
from .views import *
from .views import BlogListView


urlpatterns = [
    path('index/', index, name="index"),
    
    path('client_form/', client_form, name='client_form'),
    path('doctor/', doctor, name='doctor'),
    path('otvet/', otvet, name='otvet'),
    path('new/', BlogCreateView.as_view(), name="new")
]
