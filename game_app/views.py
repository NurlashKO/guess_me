from time import time

from django.http import JsonResponse
from rest_framework.generics import CreateAPIView
from rest_framework.parsers import JSONParser
from rest_framework.permissions import AllowAny
from auth_app.models import User
from game_app.models import Question
from game_app.serializers import GameCreateSerializer, QuestionCreateSerializer, AnswerCreateSerializer


class CreateGameAPIView(CreateAPIView):
    permission_classes = (AllowAny,)

    def post(self, request, *args, **kwargs):
        data = JSONParser().parse(request)
        data['timestamp'] = int(round(time()))
        data['host'] = User.objects.get(uuid=data['host']).id
        serializer = GameCreateSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        else:
            return JsonResponse(serializer.errors, status=400)


class CreateQuestionAPIView(CreateAPIView):
    permission_classes = (AllowAny,)

    def post(self, request, *args, **kwargs):
        data = JSONParser().parse(request)
        data['user'] = User.objects.get(uuid=data['user']).id
        serializer = QuestionCreateSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        else:
            return JsonResponse(serializer.errors, status=400)

class CreateAnswerAPIView(CreateAPIView):
    permission_classes = (AllowAny,)

    def post(self, request, *args, **kwargs):
        data = JSONParser().parse(request)
        data['user'] = User.objects.get(uuid=data['user']).id
        serializer = AnswerCreateSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        else:
            return JsonResponse(serializer.errors, status=400)
