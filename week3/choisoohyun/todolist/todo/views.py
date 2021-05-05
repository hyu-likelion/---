from django.shortcuts import render, redirect
from .models import Todo
from .forms import TodoForm

# Create your views here.
def home(request):
    todos = Todo.objects.all()
    form = TodoForm()
    return render(request, 'home.html', {'todos':todos, 'form':form})

def create(request):
    form = TodoForm(request.POST)
    if form.is_valid():
        new_todo = form.save(commit=False)
        new_todo.save()
        return redirect('home')
    return redirect('home')

def edit(request, id):
    edit_todo = Todo.objects.get(id=id)
    return render(request, 'edit.html', {'todo':edit_todo})

def update(request, id):
    update_todo = Todo.objects.get(id = id)
    update_todo.content = request.POST['content']
    update_todo.save()
    return redirect('home')

def delete(request, id):
    delete_todo = Todo.objects.get(id = id)
    delete_todo.delete()
    return redirect('home')
