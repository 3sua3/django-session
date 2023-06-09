from django.shortcuts import render, redirect
from .models import Article, Comment, Recomment
from django.contrib.auth.models import User
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
@login_required(login_url="/registration/login/")
def new(request):
    if request.method == 'POST':

        print(request.POST)

        new_article = Article.objects.create(
            title = request.POST['title'],
            content = request.POST['content'],
            category = request.POST['category'],
            author = request.user['user']
        )
        return redirect('list')
    
    return render(request, 'new.html')


def list(request):
    food = Article.objects.filter(category = 'food')
    food_number = len(food)

    next = Article.objects.filter(category = 'next')
    next_number = len(next)

    music = Article.objects.filter(category = 'music')
    music_number = len(music)

    return render(request, 'list.html', {'food_number' : food_number, 'next_number' : next_number, 'music_number' : music_number})

def detail(request, article_id):
    article = Article.objects.get(id = article_id)
    post_date = article.updated_at

    if request.method == 'POST':
        content = request.POST['content']
        Comment.objects.create(
            article = article,
            content = content,
            author = request.user,
        )
        return redirect('detail', article_id)
    
    return render(request, 'detail.html', {'article' : article, 'post_date' : post_date})

def category(request, category_name):
    category_kind = category_name
    category_articles = Article.objects.filter(category = category_name)

    return render(request, 'category.html', {'category_articles': category_articles, 'category_kind': category_kind, })
def recomment(request, article_id, comment_id):
    article = Article.objects.get(pk=article_id)
    comment = Comment.objects.get(pk=comment_id)
    post_date = article.updated_at
    if request.method == 'POST':
        recontent = request.POST['recontent']
        Recomment.objects.create(
            comment = comment,
            recontent = recontent
        )
        return redirect('recomment', article_id, comment_id)
    
    return render(request, 'recomment.html', {'article' : article, 'comment' : comment, 'post_date' : post_date})
    
def delete_comment(request, article_id, comment_id):
    comment = Comment.objects.get(id=comment_id)
    comment.delete()
    return redirect('detail', article_id)

def delete_recomment(request, article_id, comment_id, recomment_id):
    recomment = Recomment.objects.get(id=recomment_id)
    recomment.delete()
    return redirect('recomment', article_id, comment_id)

def signup(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password'] 
        User.objects.create_user(username=username, password=password)

        exist_user = User.objects.filter(username=username)

        if exist_user:
            error = "이미 존재하는 유저입니다."
            return render(request, 'registration/signup.html', {"error":error})

        new_user = User.objects.create_user(username=username, password=password)
        auth.login(request, new_user)

        return redirect('list')
    return render(request, 'registration/signup.html')

def login(request):
   if request.method == 'POST':
       username = request.POST['username']
       password = request.POST['password']

       user = auth.authenticate(username=username, password=password)

       if user is not None:
            auth.login(request, user, backend ="django.contrib.auth.backends.ModelBackend")
            return redirect('list')
            return redirect(request.GET.get('next', '/'))
       error = "아이디 또는 비밀번호가 틀립니다"
       return render(request, 'registration/login.html', {"error":error})

   return render(request, 'registration/login.html')

def logout(request):
   auth.logout(request)
   return redirect('list')