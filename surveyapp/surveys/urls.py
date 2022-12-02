from django.urls import path
from . import views

urlpatterns = [
    # TODO : set default template
    path('createsurvey/', views.create_survey, name='create survey')
]
