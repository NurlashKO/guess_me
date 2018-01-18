from django.conf.urls import url
from auth_app.views import SignUpAPIView, SignInAPIView

urlpatterns = [
    url(r'sign-up/', SignUpAPIView.as_view()),
    url(r'sign-in/', SignInAPIView.as_view()),
]
