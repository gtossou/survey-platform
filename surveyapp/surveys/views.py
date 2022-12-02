from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def create_survey(request):
    return render(request, "surveys/create-survey.html")
