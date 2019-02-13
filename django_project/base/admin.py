# coding=utf-8
from django.contrib import admin
from .models.questionnaire import Questionnaire


class QuestionnaireAdmin(admin.ModelAdmin):

    list_display = ('question', 'unique_id')


admin.site.register(Questionnaire, QuestionnaireAdmin)


