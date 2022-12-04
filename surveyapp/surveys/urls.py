from django.urls import path

from .views import CreateSurveyView

urlpatterns = [
    # TODO : set default template
    # path("create_survey", CreateSurveyView.as_view(), name="create survey")
    path("create_survey", CreateSurveyView, name="create survey")
]
