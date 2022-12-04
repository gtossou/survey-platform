from django.shortcuts import render
from django.views.generic.list import ListView
from .models import Question, Answer
# Create your views here.


class CreateSurveyView(ListView):
    # return render(request, "surveys/create-survey.html")ù
    model = Question


# def create_survey(request):
#     return render(request, "surveys/create_survey.html")
