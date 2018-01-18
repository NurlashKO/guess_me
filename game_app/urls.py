from django.conf.urls import url
from game_app.views import CreateGameAPIView, CreateQuestionAPIView, CreateAnswerAPIView

urlpatterns = [
    url(r'create/$', CreateGameAPIView.as_view()),
    url(r'create/question/$', CreateQuestionAPIView.as_view()),
    url(r'create/answer/$', CreateAnswerAPIView.as_view()),
]