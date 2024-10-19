from django.contrib.auth.models import User
from django.db import models
from ckeditor.fields import RichTextField
# Create your models here.
class News(models.Model):
    title = models.CharField(max_length=200,verbose_name='Yanglik sarlavhasi')
    text = RichTextField(verbose_name='Yanglik matni')
    image = models.ImageField(upload_to='news_images/')
    author = models.ForeignKey(User,on_delete=models.CASCADE)
    created_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class Contact(models.Model):
    name = models.CharField(max_length=200, verbose_name="foydalanuvchi ismi", blank=False, null=False)
    email = models.EmailField(max_length=200,verbose_name='foydalanuvchi emaili')
    message = models.TextField(verbose_name='foydalanuvchi xabari')
    created_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Termin(models.Model):
    name = models.CharField(max_length=200,verbose_name='Termin nomi')
    description = RichTextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Article(models.Model):
    title = models.CharField(max_length=200, verbose_name='Maqola sarlavhasi')
    full_name = models.CharField(max_length=200, verbose_name='Maqola egasi FISH')
    work_study_place = models.CharField(max_length=200, verbose_name="O'qish yoki ish joyi, ilmiy unvoni")
    anotatsiya = RichTextField(verbose_name='Maqola anotatsiyasi')
    key_words = models.CharField(max_length=200, verbose_name='Maqola kalit sozlari')
    kirish = RichTextField(verbose_name='Maqola kirish qismi')
    main_body =  RichTextField(verbose_name='Maqola asosiy qismi')
    file = models.FileField(upload_to='maqola_files/')
    created_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

