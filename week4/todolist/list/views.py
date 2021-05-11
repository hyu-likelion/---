from django.shortcuts import render, redirect
from .models import Todolist
from .forms import TodolistForm


def home(request):
    todolist = Todolist.objects.all()
    form = TodolistForm()
    return render(request, "home.html", {'todolist': todolist, 'form': form})


def create(request):
    form = TodolistForm(request.POST)
    if form.is_valid():
        new_list = form.save(commit=False)
        new_list.save()
        return redirect('home')
    return redirect('home')


def edit(request, id):
    edit_list = Todolist.objects.get(id=id)
    return render(request, 'edit.html', {'list': edit_list})


def update(request, id):
    update_list = Todolist.objects.get(id=id)
    update_list.body = request.POST['body']
    update_list.save()
    return redirect('home')


def delete(request, id):
    delete_list = Todolist.objects.get(id=id)
    delete_list.delete()
    return redirect('home')
