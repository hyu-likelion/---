from django.db import models

# Create your models here.


class Quiz(models.Model):
    question = models.TextField()
    choice1 = models.CharField(max_length=10)
    choice2 = models.CharField(max_length=10)
    choice3 = models.CharField(max_length=10)
    choice4 = models.CharField(max_length=10)
    choice5 = models.CharField(max_length=10)

    # def __str__(self):
    #     return self.question
