from django.shortcuts import render, redirect
from .models import Article
# Create your views here.
def new(request):
    if request.method == 'POST':

        print(request.POST)

        new_article = Article.objects.create(
            title = request.POST['title'],
            content = request.POST['content'],
            category = request.POST['category'],
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
    return render(request, 'detail.html', {'article' : article, 'post_date' : post_date})

def category(request, category_name):
    category_kind = category_name
    category_articles = Article.objects.filter(category = category_name)

    return render(request, 'category.html', {'category_articles': category_articles, 'category_kind': category_kind, })