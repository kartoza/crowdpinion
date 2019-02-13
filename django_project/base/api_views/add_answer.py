# coding=utf-8
from django.http import JsonResponse
from rest_framework import serializers
from rest_framework.views import APIView
from ..models.questionnaire import Questionnaire


class AddAnswer(APIView):
    """API to get answers."""

    def post(self, request, unique_id):
        try:
            question = Questionnaire.objects.get(unique_id=unique_id)
            answers = question.answers
            new_answer = request.POST.get('answer')
            if answers:
                answers = answers + ', ' + new_answer
            else:
                answers = new_answer
            question.answers = answers
            question.save()

            return JsonResponse({
                'status': 'success'
            })

        except Questionnaire.DoesNotExist:
            msg = 'Question does not exist.'
            raise serializers.ValidationError(msg)