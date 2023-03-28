from django.forms import ModelForm
from .models import Client

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