# coding=utf-8
"""Urls for changelog application."""
from django.conf.urls import url
from .api_views.get_answers import GetAnswers
from .api_views.add_answer import AddAnswer
from .views import Home, custom_404
from .views.question import (
    QuestionCreateView,
    ResultsView,
    AnswerView,
    AnswersAsTextView,
    QuestionsView)

urlpatterns = [
    # basic app views
    url(regex=r'^api/get-answers/(?P<unique_id>[\w-]+)/$',
        view=GetAnswers.as_view(),
        name='get-answers'),
    url(regex=r'^api/add-answers/(?P<unique_id>[\w-]+)/$',
        view=AddAnswer.as_view(),
        name='add-answers'),
    url(regex=r'^results/(?P<unique_id>[\w-]+)/$',
        view=ResultsView.as_view(),
        name='results'),
    url(regex=r'^answers/(?P<unique_id>[\w-]+)/$',
        view=AnswersAsTextView.as_view(),
        name='answers-as-text'),
    url(regex=r'^all-questions/$',
        view=QuestionsView.as_view(),
        name='all-questions'),
    # Watch this next one is a catch - all!
    url(regex=r'^(?P<unique_id>[\w-]+)/$',
        view=AnswerView.as_view(),
        name='answers'),
    url(regex=r'^$',
        view=QuestionCreateView.as_view(),
        name='home'),

]

# Prevent cloudflare from showing an ad laden 404 with no context
handler404 = custom_404

