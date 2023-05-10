from django.urls import path
from .views import *



urlpatterns = [
    path('index/', index, name="index"),
    
    
    path('client_form/', PatientCreateView.as_view(), name='client_form'),
    path('doctor/', doctor, name='doctor'),
    path('otvet/', otvet, name='otvet'),
    path('new/', BlogCreateView.as_view(), name="new"),
    path('history-form/', HistoryCreateView.as_view(), name="history_form"),
    path('history/', HistoryListView, name="history"),
    path('history_list/<int:pk>', history_info, name='history_list'),
    path('departament/', DepartementViews, name="departament"),
    path('departament/<int:pk>', det_view, name="detail_info"),
]
