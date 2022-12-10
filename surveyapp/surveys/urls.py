from django.urls import path

from .views import createSurveyView, surveyListView, renderSurveyView

urlpatterns = [
    # TODO : set default template
    # path("create_survey", CreateSurveyView.as_view(), name="create survey")
    path("create_survey", createSurveyView, name="create survey"),
    path("survey_list", surveyListView.as_view(), name="survey list"),
    path("render_survey/<str:survey_link>",
         renderSurveyView, name="render survey")
]
