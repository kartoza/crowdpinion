# coding=utf-8
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic import CreateView, DetailView, TemplateView
from django.urls import reverse_lazy
from ..models.questionnaire import Questionnaire


class QuestionCreateView(SuccessMessageMixin, CreateView):
    """View to create question."""

    model = Questionnaire
    template_name = 'landing_page.html'
    fields = ['question']
    success_message = 'Thank you for submitting your CrowdPinion question!'

    def get_success_url(self, **kwargs):
        return reverse_lazy(
            'results', kwargs={'unique_id': self.object.unique_id})


class ResultsView(DetailView):
    """View to see question and collected answers."""

    context_object_name = 'questionnaire'
    template_name = 'results.html'
    model = Questionnaire

    def get_object(self):
        return Questionnaire.objects.get(unique_id=self.kwargs['unique_id'])

    def get_context_data(self, **kwargs):

        context = super(ResultsView, self).get_context_data(**kwargs)
        current_site = self.request.META['HTTP_HOST']
        unique_id = self.object.unique_id
        scheme = self.request.is_secure() and "https" or "http"
        context['result_site'] = \
            '{}://{}/results/{}/'.format(scheme, current_site, unique_id)
        context['current_site'] = \
            '{}://{}/{}/'.format(scheme, current_site, unique_id)
        return context


class AnswerView(TemplateView):
    """View for participants where they can submit answers."""

    template_name = 'answer.html'

    def get_context_data(self, **kwargs):
        context = super(AnswerView, self).get_context_data(**kwargs)
        unique_id = kwargs.pop('unique_id')
        try:
            question = Questionnaire.objects.get(unique_id=unique_id)
            context['question'] = question.question
        except:
            context['question'] = 'No questions asked here.'
        context['question_id'] = unique_id
        return context

class AnswersAsTextView(TemplateView):
    """View for answers as plain text."""

    template_name = 'answers_as_text.txt'

    def get_context_data(self, **kwargs):
        context = super(AnswerView, self).get_context_data(**kwargs)
        unique_id = kwargs.pop('unique_id')
        try:
            question = Questionnaire.objects.get(unique_id=unique_id)
            context['answers'] = question.answers.split(',')
        except:
            context['answers'] = 'No questions asked here.'
        return context

