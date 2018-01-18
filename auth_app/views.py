from json import dumps
from django.contrib.auth import get_user_model, authenticate
from django.http import JsonResponse
from rest_framework.generics import CreateAPIView, get_object_or_404
from rest_framework.parsers import JSONParser
from rest_framework.permissions import AllowAny
from rest_framework.views import APIView
from auth_app.models import User
from auth_app.serializers import UserCreateSerializer


class SignUpAPIView(CreateAPIView):
    permission_classes = (AllowAny,)
    serializer_class = UserCreateSerializer


class SignInAPIView(APIView):
    permission_classes = (AllowAny,)

    def post(self, request):
        data = JSONParser().parse(request)
        credentials = {
            get_user_model().USERNAME_FIELD: data['username'],
            'password': data['password']
        }
        is_authenticated = authenticate(**credentials)
        if is_authenticated is not None:
            user = get_object_or_404(User, username=data['username'])
            result = {'uuid': user.uuid}
            return JsonResponse(dumps(result), status=201, safe=False)
