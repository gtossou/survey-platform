from django.shortcuts import render
from django.views.generic.list import ListView
from django.forms import formset_factory
from .models import Question, Answer, Survey
from .forms import QuestionForm, SurveyForm
# Create your views here.


# class CreateSurveyView(ListView):
#     # return render(request, "surveys/create-survey.html")ù
#     model = Question

class surveyListView(ListView):

    # specify the model for list view
    model = Survey


def createSurveyView(request):
    if request.method == "POST":
        survey_form = SurveyForm(request.POST)
        question_form = QuestionForm(request.POST)
        if survey_form.is_valid() and question_form.is_valid():
            survey = survey_form.save()
            question = question_form.save(commit=False)
            question.survey = survey
            question.save()
    else:
        survey_form = SurveyForm()
        question_form = QuestionForm()

    return render(request, 'surveys/create_survey.html', {'question_form': question_form, 'survey_form': survey_form})


class renderSurveyView(ListView):

    # specify the model for list view
    model = Survey


def renderSurveyView(request, survey_link):
    return render(request, 'render_survey.html', {'survey_link': survey_link})

# def surveyListView(request):
#     context = {}

#     # creating a formset
#     surveysFormset = formset_factory(ListSurveyForm)
#     formset = surveysFormset()

#     # Add the formset to context dictionary
#     context['formset'] = formset
#     return render(request, "surveys/survey_list.html", context)
