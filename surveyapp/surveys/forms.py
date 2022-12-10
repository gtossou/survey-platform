from django import forms
from .models import Question, Survey


class QuestionForm(forms.ModelForm):

    class Meta:
        model = Question
        fields = ('type', 'question_title', 'description', 'options')


class SurveyForm(forms.ModelForm):

    class Meta:
        model = Survey
        fields = ('title', 'description')
