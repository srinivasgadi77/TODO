from django.shortcuts import render, redirect
from django.http import HttpResponse

from .models import  Todo
# Create your views here.

def index(request):
    # return HttpResponse('<h1>Hellow World</h1>')
    todos = Todo.objects.all()
    context = {
        'todos' : todos
    }

    return render(request, 'todos\index.html',context)

def details(request, id):
    print('ID valu' , id )
    todo=Todo.objects.get(id=id)

    context = {
        'todo' : todo
    }
    return render(request, 'todos\details.html',context)

def add(request):
    if request.method == 'POST':
        title = request.POST['title']
        text = request.POST['text']
        todo = Todo(title=title, text=text)

        todo.save()

        return redirect('/todos')
    else:
        return render(request, r'todos\add.html')
