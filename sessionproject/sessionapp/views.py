from django.shortcuts import render
from .models import Quiz

# Create your views here.


def main(request):
    quizs = Quiz.objects.all()
    return render(request, 'main.html', {'quizs': quizs})


def vote(request):
    return render(request, 'vote.html')


def vote(request):

    return render(request, 'result.html', )
