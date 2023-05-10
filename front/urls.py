from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name="core"),
    path('dep/', dep, name='dep'),
    path('dep/<int:pk>/', dep_view,),
    path('onas/', onas, name='onas')

]
