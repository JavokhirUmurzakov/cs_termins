from django.contrib import admin
from .models import Contact,Termin,News,Article

@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ['title','text','author','image','created_time']
    search_fields = ['title']


@admin.register(Contact)
class NewsAdmin(admin.ModelAdmin):
    list_display = ['name','email','message','created_time']
    search_fields = ['name']


@admin.register(Termin)
class NewsAdmin(admin.ModelAdmin):
    list_display = ['name','description','author','created_time']
    search_fields = ['name']

@admin.register(Article)
class NewsAdmin(admin.ModelAdmin):
    list_display = ['id','title','anotatsiya','created_time','key_words']
    search_fields = ['name']