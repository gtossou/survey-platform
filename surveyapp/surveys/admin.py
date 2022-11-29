from django.contrib import admin

from .models import Question, Survey


admin.site.register(Question)
admin.site.register(Survey)


# @admin.register(Question)
# class QuestionAdmin(admin.ModelAdmin):
#     pass
#     # list_display = [field.name for field in
#     #                 Question._meta.get_fields()]


# @admin.register(QuestionItem)
# class QuestionItemAdmin(admin.ModelAdmin):
#     list_display = [field.name for field in
#                     QuestionItem._meta.get_fields()]
