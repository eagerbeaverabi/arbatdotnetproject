from django.shortcuts import render, get_object_or_404, redirect
from .forms import LoginForm, RegisterationForm
from .models import Blogger, Article
from django.http import Http404

global logged_in
logged_in = False

def is_logged_in():
    if not logged_in:
        raise Http404()

def login(request):
    if request.method != 'POST':
        form = LoginForm()
    else:
        form = LoginForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            get_object_or_404(Blogger,
                              username=username, password=password)
            global logged_in
            logged_in = True
            return redirect('blogger:home', username=username)
    context = {'form': form}
    return render(request, 'blogger/entrance/login.html', context)

def register(request):
    if request.method != 'POST':
        form = RegisterationForm()
    else:
        form = RegisterationForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            if Blogger.objects.filter(username=username):
                raise Http404
            fullname = form.cleaned_data['fullname']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            blogger = Blogger(username=username,
                              email=email, password=password,
                              fullname=fullname)
            blogger.save()
            return redirect('blogger:login')
    context = {'form': form}
    return render(request, 'blogger/entrance/register.html', context)

def logout(request):
    global logged_in
    logged_in = False
    return redirect('blogger:login')

def home(request, username):
    is_logged_in()
    blogger = get_object_or_404(Blogger, username=username)
    articles = Article.objects.filter(author=blogger)
    context = {
        'username': blogger.username,
        'fullname': blogger.fullname,
        'articles': articles,
        }
    return render(request, 'blogger/home/home.html', context)

def profile(request, username):
    is_logged_in()
    blogger = get_object_or_404(Blogger, username=username)
    data = request.POST
    if data:
        blogger.username = data['username']
        blogger.email = data['email']
        blogger.password = data['password']
        blogger.fullname = data['fullname']
        blogger.description = data['description']
        blogger.save()
        blogger.save()
    context = {
        'blogger':blogger,
        'username':blogger.username,
        }
    return render(request, 'blogger/home/profile.html', context)

def workspace(request, username, article_id=None, delete=0):
    is_logged_in()
    if delete == 1:
        article = get_object_or_404(Article, id=article_id)
        article.delete()
        return redirect('blogger:home', username=username)
    if request.method == 'POST':
        blogger = get_object_or_404(Blogger, username=username)
        data = request.POST
        if data:
            title = data['title']
            body = data['body']
            if article_id:
                article = get_object_or_404(Article, id=article_id)
                article.title = title
                article.body = body
                article.save()
                return redirect('blogger:home', username=username)
            else:
                blogger.article_set.create(title=title, body=body)
                return redirect('blogger:home', username=username)
    context = {'username':username, 'id':article_id,}
    if article_id:
        article = get_object_or_404(Article, id=article_id)
        context['article'] = article
    return render(request, 'blogger/home/workspace.html', context)

def articles(request, username):
    is_logged_in()
    articles = Article.objects.all()
    blogger = get_object_or_404(Blogger, username=username)
    if len(articles) == len(Article.objects.filter(author=blogger)):
        count = 0
    else:
        count = 1
    context = {"username":username, "articles": articles, "count": count}
    return render(request, 'blogger/home/articles.html', context)

def bloggers(request, username, author=None):
    is_logged_in()
    if author:
        blogger = get_object_or_404(Blogger, id=author)
        number_of_articles = len(Article.objects.filter(author=blogger))
        context = {"username": username, "blogger": blogger, "author": author,
                    "number_of_articles":number_of_articles}
    else:
        bloggers = Blogger.objects.all()
        context = {"username": username, "bloggers": bloggers, "author": None}
    return render(request, 'blogger/home/bloggers.html', context)