from django.urls import path
from .views import home,contact,termins,blogs,blog_id,articles,article_one
urlpatterns = [
    path('',home,name='home_page'),
    path('blogs/',blogs,name='blogs_page'),
    path('articles/',articles,name='articles_page'),
    path('article-one/<int:id>/',article_one,name='article_one_page'),
    path('contact/',contact,name='contact_page'),
    path('termins/<int:page>/',termins,name='termins_page'),
    # path('blog/<int:pk>/',blog_id,name='detail_page'),
]
