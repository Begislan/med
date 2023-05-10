from django import forms
from django.forms import ModelForm
from .models import Client, History

class ClientForm(ModelForm):
    class Meta:
        model = Client
        fields = '__all__'
    
from django.forms import ModelForm
from.models import Post

class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = ['title','body']

class HistoryForm(ModelForm):

    class Meta:
        model = History
        fields = '__all__'