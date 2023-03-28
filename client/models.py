from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from ckeditor_uploader.fields import RichTextUploadingField


# Create your models here.
class Client(models.Model):
    FEMALE_CHOICES = (
        ('0', 'Аял'),
        ("1", 'Эркек')
    )

    name = models.CharField(max_length=50, verbose_name="Имя")
    sourname = models.CharField(max_length=250, verbose_name="Фамилия")
    phone = PhoneNumberField(unique=True, verbose_name='Телефон номер', default="+996")
    region = models.ForeignKey('Region', on_delete=models.CASCADE, verbose_name="Регион")
    doctor = models.ForeignKey('Doctor', on_delete=models.SET_NULL, null=True, verbose_name="Врач")
    female = models.CharField(max_length=1, choices=FEMALE_CHOICES, verbose_name="Пол")
    date = models.DateField(auto_now_add=True)
    time = models.TimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.name

    # def get_absolute_url(self):
    #     success_url = reverse_lazy("otvet.html")


class Region(models.Model):
    title = models.CharField(max_length=250)
    slug = models.SlugField(unique=True, help_text='Поля автоматический заполняется!')

    def __str__(self) -> str:
        return self.title


class Doctor(models.Model):
    name = models.CharField(max_length=250)
    slug = models.SlugField(unique=True, help_text='Поля автоматический заполняется!')

    def __str__(self) -> str:
        return self.name


class Post(models.Model):
    title = models.CharField(max_length=255, verbose_name='Тема поста')
    # body = models.TextField()
    body = RichTextUploadingField(verbose_name='Пост:')  # CKEditor Rich Text Field

    def __str__(self):
        return self.title
