from django.shortcuts import render,redirect
from .models import Todo
# Create your views here.

def home(request):
    tasks = Todo.objects.all()
    return render(request, 'home.html', {'tasks': tasks,})

def new(request):
    if request.method == 'POST':
        new_Todo = Todo.objects.create(
            title = request.POST['title'],
            content = request.POST['content'],
            deadline_dt = request.POST['deadline_dt'],
        )
        return redirect('home')
    return render(request, 'new.html')

def detail(request, detail_pk):
    tasks= Todo.objects.filter(pk = detail_pk)
    return render(request, 'detail.html', {'tasks': tasks})

def update(request, detail_pk):
    tasks= Todo.objects.filter(pk = detail_pk)
    if request.method == 'POST':
        Todo.objects.filter(pk = detail_pk).update(
            title = request.POST['title'],
            content = request.POST['content'],
            deadline_dt = request.POST['deadline_dt'],
        )
        return redirect('home')
    return render(request, 'update.html', {'tasks' : tasks})

def delete(request, detail_pk):
    tasks = Todo.objects.filter(pk = detail_pk)
    tasks.delete()
    return redirect('home')