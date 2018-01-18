from django.db.models import Model, TextField, ForeignKey, CASCADE, IntegerField

from auth_app.models import User


class Game(Model):
    name = TextField(max_length=256, null=False, blank=False)
    host = ForeignKey(to=User, related_name='games', on_delete=CASCADE)
    timestamp = IntegerField()

    def __str__(self):
        return 'id: ' + str(self.id) + ', name: ' + self.name


class Question(Model):
    url = TextField(max_length=128, null=False, blank=False)
    start_time = IntegerField(null=False, blank=False)
    finish_time = IntegerField(null=False, blank=False)
    game = ForeignKey(to=Game, related_name='questions', on_delete=CASCADE)
    a = TextField(max_length=128, null=False, blank=False)
    b = TextField(max_length=128, null=False, blank=False)
    c = TextField(max_length=128, null=False, blank=False)
    d = TextField(max_length=128, null=False, blank=False)

    def __str__(self):
        return 'id: ' + str(self.id) + ', url: ' + self.url


class Answer(Model):
    question = ForeignKey(to=Question, related_name='answers', on_delete=CASCADE)
    user = ForeignKey(to=User, related_name='answers', on_delete=CASCADE)
    content = TextField(max_length=128, null=False, blank=False)

    def __str__(self):
        return 'id: ' + str(self.id) + ', content: ' + self.content
