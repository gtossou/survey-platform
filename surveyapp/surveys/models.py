from django.db import models
import uuid


class Survey(models.Model):
    title = models.CharField(max_length=400)
    description = models.TextField(null=True)
    link = models.CharField()
    created = models.UUIDField(
        default=uuid.uuid4, unique=True, primary_key=True, editable=False)


# class User

class Question(models.Model):
    title = models.TextField(null=True)
    type = models.CharField(null=True)
    is_mandatory = models.BooleanField(default=True)
    id = models.UUIDField(
        default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    survey = models.ForeignKey(Survey, on_delete=models.CASCADE)


class Answer(models.Model):
    content = models.TextField()
    id = models.UUIDField(
        default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    users = models.ManyToManyField(User)
    questions = models.ManyToManyField(Question)
