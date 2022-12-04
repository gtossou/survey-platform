from django.shortcuts import render
from django.views.generic.list import ListView
from .models import Question, Answer, Survey
from .forms import QuestionForm, SurveyForm
# Create your views here.


# class CreateSurveyView(ListView):
#     # return render(request, "surveys/create-survey.html")ù
#     model = Question


def CreateSurveyView(request):
    question_form = QuestionForm()
    survey_form = SurveyForm()
    return render(request, 'surveys/create_survey.html', {'question_form': question_form, 'survey_form': survey_form})


# def create_survey(request):
#     return render(request, "surveys/create_survey.html")
