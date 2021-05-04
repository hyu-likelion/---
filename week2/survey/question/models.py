from django.db import models


class survey(models.Model):

    survey_idx = models.AutoField(primary_key=True)
    # 문제
    question = models.TextField(null=True)
    # 선택지 1~4
    answer1 = models.TextField(null=True)
    answer2 = models.TextField(null=True)
    answer3 = models.TextField(null=True)
    answer4 = models.TextField(null=True)

    status = models.CharField(max_length=1, default="y")


class Answer(models.Model):
    answer_idx = models.AutoField(primary_key=True)
    survey_idx = models.IntegerField()
    answer = models.TextField()
