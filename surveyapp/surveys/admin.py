from django.contrib import admin

from .models import Question, QuestionItem


@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = [field.name for field in
                    Question._meta.get_fields()]


@admin.register(QuestionItem)
class QuestionItemAdmin(admin.ModelAdmin):
    list_display = [field.name for field in
                    QuestionItem._meta.get_fields()]
