from django.contrib.auth.models import User

from django.db import models
import jsonfield


class Survey(models.Model):
    title = models.CharField(max_length=400)
    description = models.TextField(null=True)
    link = models.URLField(max_length=500)
    created = models.DateTimeField(auto_now_add=True)


class Question(models.Model):
    title = models.TextField(null=True)
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
        default=SHORT_ANSWER,
    )
    is_mandatory = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    survey = models.ForeignKey(Survey, on_delete=models.CASCADE)


class QuestionItem(models.Model):
    isShortAnswer = models.BooleanField(default=False)
    short_answer_content = models.CharField()
    isParagraph = models.BooleanField(default=False)
    paragraph_content = models.CharField()
    isRadio = models.BooleanField(default=False)
    radio_content = jsonfield.JSONField("RadioData", default={})
    isCheckbox = models.BooleanField(default=False)
    checkbox_content = jsonfield.JSONField("CheckboxData", default={})
    isDropdown = models.BooleanField(default=False)
    # TODO: Field to store list?
    dropdown_content = models.CharField()
    question = models.ForeignKey(Question, on_delete=models.CASCADE)


class Answer(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    question_item = models.ForeignKey(QuestionItem, on_delete=models.CASCADE)
    # orm create new row created gets set automatically = when question gets
    # opened
    created = models.DateTimeField(auto_now_add=True)
    # orm upon update (answering question), set content AND answered datetime
    content = models.TextField()
    answered = models.DateTimeField(null=True, blank=True)
