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

    class Meta:
        verbose_name = "Клиент"
        verbose_name_plural = "Клиент"

class Region(models.Model):
    title = models.CharField(max_length=250)
    slug = models.SlugField(unique=True, help_text='Поля автоматический заполняется!')

    def __str__(self) -> str:
        return self.title

    class Meta:
        verbose_name = "Регион"
        verbose_name_plural = "Регион"

class Doctor(models.Model):
    department = models.ForeignKey("Departament", on_delete=models.CASCADE)
    name = models.CharField(max_length=250)
    slug = models.SlugField(unique=True, help_text='Поля автоматический заполняется!')
    img = models.ImageField(upload_to='media/photo_doc')

    def __str__(self) -> str:
        return self.name
    
    class Meta:
        verbose_name = "Врачи"
        verbose_name_plural = "Врачи"

class Post(models.Model):
    title = models.CharField(max_length=255, verbose_name='Тема поста')
    body = RichTextUploadingField(verbose_name='Пост:')  # CKEditor Rich Text Field

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = "Новости"
        verbose_name_plural = "Новости"

class Departament(models.Model):
    region = models.ForeignKey(Region, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    slug = models.SlugField(help_text="Поля автоматически заполняется: ")
    info = RichTextUploadingField(verbose_name="Информация по отделении: ")
    
    def __str__(self) -> str:
        return self.name
    
    class Meta:
        verbose_name = "Отделение"
        verbose_name_plural = "Отделении"

