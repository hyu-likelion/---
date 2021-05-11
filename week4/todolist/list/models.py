from django.db import models


class Todolist(models.Model):
    body = models.CharField(max_length=100)

    def __str__(self):
        return self.body
