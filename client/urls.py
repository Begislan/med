from django.urls import path
from .views import *



urlpatterns = [
    path('index/', index, name="index"),
    
    path('client_form/', client_form, name='client_form'),
    path('doctor/', doctor, name='doctor'),
    path('otvet/', otvet, name='otvet'),
    path('new/', BlogCreateView.as_view(), name="new"),
    path('departament/', DepartementViews, name="departament"),
    path('departament/<int:pk>', det_view, name="detail_info"),
]
