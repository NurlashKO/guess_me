from rest_framework.serializers import ModelSerializer

from game_app.models import Game, Question, Answer


class GameCreateSerializer(ModelSerializer):
    class Meta:
        model = Game
        fields = ('id', 'name', 'host', 'timestamp',)

    def create(self, validated_data):
        game = Game(**validated_data)
        game.save()
        return game


class QuestionCreateSerializer(ModelSerializer):
    class Meta:
        model = Question
        fields = ('url', 'start_time', 'finish_time', 'game', 'a', 'b', 'c', 'd',)

    def create(self, validated_data):
        question = Question(**validated_data)
        question.save()
        return question

class AnswerCreateSerializer(ModelSerializer):
    class Meta:
        model = Answer
        fields = ('question', 'user', 'content')

    def create(self, validated_data):
        answer = Answer(**validated_data)
        answer.save()
        return answer