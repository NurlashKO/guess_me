from django.contrib import admin

# Register your models here.
from game_app.models import Game, Question, Answer

admin.site.register(Game)
admin.site.register(Question)
admin.site.register(Answer)