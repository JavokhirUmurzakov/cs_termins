from django.shortcuts import render, redirect
from .models import News,Contact,Termin,Article
from .forms import ContactForm
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Q
# Create your views here.
def home(request):
    news = News.objects.all()
    context = {
        'news': news,
    }
    return render(request,'index.html',context)

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']

            contact = Contact.objects.create(name=name, email=email, message=message)
            contact.save()

            # Send an email

            return redirect('home_page')
    else:
        form = ContactForm()
    return render(request,'contact.html',{'form':form})

def blogs(request):
    news = News.objects.all()
    context = {
        'news': news,
    }
    return render(request,'blogs.html',context)

def articles(request):
    article = Article.objects.all()
    context = {
        'article': article,
    }
    return render(request,'articles.html',context)

def article_one(request,id):
    article_one = Article.objects.get(id=id)
    context = {
        'article_one': article_one,
    }
    return render(request,'article_one.html',context)

def blog_id(request,pk):
    news_id = News.objects.get(id=pk)
    context = {
        'news_id': news_id
    }
    return render(request,'blog_detail.html',context)

def termins(request,page=1):
    termin = 0
    if 'q' in request.GET:
        q = request.GET['q']
        termin = Termin.objects.filter(Q(name__icontains=q) | Q(description__icontains=q))
        paginator = Paginator(termin, 10)
        try:
            termin = paginator.page(page)
        except PageNotAnInteger:
            termin = paginator.page(1)
        except EmptyPage:
            termin = paginator.page(paginator.num_pages)
    else:
        termin = Termin.objects.order_by('name').values()
        paginator = Paginator(termin, 10)
        try:
            termin = paginator.page(page)
        except PageNotAnInteger:
            termin = paginator.page(1)
        except EmptyPage:
            termin = paginator.page(paginator.num_pages)
        q = None

    context = {
        'objects': termin,
        'termin': termin,
        'q': q,
    }
    return render(request,'termins.html',context=context)
