# coding=utf-8
from django.http import JsonResponse
from rest_framework import serializers
from rest_framework.views import APIView
from ..models.questionnaire import Questionnaire


class GetAnswers(APIView):
    """API to get answers."""

    def get(self, request, unique_id):
        try:
            question = Questionnaire.objects.get(unique_id=unique_id)
            answers = question.answers
            return JsonResponse({
                'answers': answers
            })
        except Questionnaire.DoesNotExist:
            msg = 'Object does not exist.'
            raise serializers.ValidationError(msg, code='authorization')