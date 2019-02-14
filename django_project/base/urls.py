# coding=utf-8
"""Urls for changelog application."""
from django.conf.urls import url
from .api_views.get_answers import GetAnswers
from .api_views.add_answer import AddAnswer
from .views import Home, custom_404
from .views.question import QuestionCreateView, ResultsView, AnswerView

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
    url(regex=r'^(?P<unique_id>[\w-]+)/$',
        view=AnswerView.as_view(),
        name='answers'),
    url(regex=r'^$',
        view=QuestionCreateView.as_view(),
        name='home'),
]

# Prevent cloudflare from showing an ad laden 404 with no context
handler404 = custom_404

