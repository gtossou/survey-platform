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
    is_mandatory = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)
    survey = models.ForeignKey(Survey, on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class QuestionItem(models.Model):
    isShortAnswer = models.BooleanField(default=False)
    short_answer_content = models.CharField(max_length=400)
    isParagraph = models.BooleanField(default=False)
    paragraph_content = models.CharField(max_length=3000)
    isRadio = models.BooleanField(default=False)
    radio_content = models.JSONField("RadioData", default=dict)
    isCheckbox = models.BooleanField(default=False)
    checkbox_content = models.JSONField("CheckboxData", default=dict)
    isDropdown = models.BooleanField(default=False)
    # TODO: Field to store list?
    dropdown_content = models.CharField(max_length=1200)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)

    def __str__(self):
        return self.isShortAnswer


class Answer(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    question_item = models.ForeignKey(QuestionItem, on_delete=models.CASCADE)
    # orm create new row created gets set automatically = when question gets
    # opened
    created = models.DateTimeField(auto_now_add=True)
    # orm upon update (answering question), set content AND answered datetime
    content = models.TextField()
    answered = models.DateTimeField(null=True, blank=True)

    # TODO: Implement logic jump

    # TODO: You can assign any JSON-encodable object to this field. It will be JSON-encoded before being stored in the database as a text value and it will be turned back into a python list/dict/string upon retrieval from the database.
    # There is also a TypedJSONField, that allows you to define data types that must be included within each object in the array. More documentation to follow
