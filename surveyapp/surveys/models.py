from django.contrib.auth.models import User

from django.db import models
import uuid


class Survey(models.Model):
    title = models.CharField(max_length=400)
    description = models.TextField(null=True)
    link = models.CharField(max_length=100, blank=True,
                            unique=True, default=uuid.uuid4)
    created = models.DateTimeField(auto_now_add=True)


class Question(models.Model):
    # TODO: make choicelist to have a fixed set of types
    QUESTION_TYPES = [
        ('SHORT_ANSWER', 'Short answer'),
        ('PARAGRAPH', 'Paragraph answer'),
        ('RADIO', 'Radio options'),
        ('CHECKBOXES', 'Checkboxes'),
        ('DROPDOWN', 'Dropdown list')
    ]
    type = models.CharField(
        max_length=32,
        choices=QUESTION_TYPES,
        # TODO : use values instead of number
        default=QUESTION_TYPES[0],
    )
    survey = models.ForeignKey(Survey, on_delete=models.CASCADE)
    question_title = models.CharField(max_length=400)
    description = models.TextField(null=True, blank=True)
    is_mandatory = models.BooleanField(default=True)
    options = models.JSONField(
        "OptionData", default=dict, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.question_title
    # TODO : add ordering


class Answer(models.Model):
    # user = models.ForeignKey(User, on_delete=models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    # orm create new row created gets set automatically = when question gets
    # opened
    created = models.DateTimeField(auto_now_add=True)
    # orm upon update (answering question), set content AND answered datetime
    content = models.TextField()
    answered = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f"{self.user} {self.question_item}"

    # TODO: Implement logic jump
    # TODO: You can assign any JSON-encodable object to this field. It will be JSON-encoded before being stored in the database as a text value and it will be turned back into a python list/dict/string upon retrieval from the database.
    # There is also a TypedJSONField, that allows you to define data types that must be included within each object in the array. More documentation to follow
