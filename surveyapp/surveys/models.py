from django.contrib.auth.models import User
from django.db import models


class Survey(models.Model):
    title = models.CharField(max_length=400)
    description = models.TextField(null=True)
    link = models.URLField(max_length=500)
    created = models.DateTimeField(auto_now_add=True)


class Question(models.Model):
    title = models.TextField(null=True)
    # TODO: make choicelist to have a fixed set of types
    type = models.CharField(null=True, max_length=20)
    is_mandatory = models.BooleanField(default=True)
    survey = models.ForeignKey(Survey, on_delete=models.CASCADE)


class Answer(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    # orm create new row created gets set automatically = when question gets
    # opened
    created = models.DateTimeField(auto_now_add=True)
    # orm upon update (answering question), set content AND answered datetime
    content = models.TextField()
    answered = models.DateTimeField(null=True, blank=True)
