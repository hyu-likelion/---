from django import forms
from .models import Todolist


class TodolistForm(forms.ModelForm):
    class Meta:
        model = Todolist
        fields = ['body']
        widgets = {
            'body': forms.TextInput(attrs={
                'style': 'text-align: left; font-size: 15px;',
                'placeholder': 'Input your to do list'}),
        }
