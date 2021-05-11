from django.shortcuts import render, redirect
from .models import Todo
from .forms import TodoForm

# Create your views here.


def home(request):
    todos = Todo.objects.all()
    form = TodoForm()
    return render(request, 'home.html', {'todos': todos, 'form': form})


def create(request):
    form = TodoForm(request.POST)
    if form.is_valid():
        form.save()
    return redirect('home')


def delete(request, id):
    delete_todo = Todo.objects.get(id=id)
    delete_todo.delete()
    return redirect('home')


def update(reqest, id):
    update_todo = Todo.objects.get(id=id)
    update_todo.body = request.POST['body']
    update_todo.save()
    return redirect('home')
