from uuid import uuid4
from django.contrib.auth.models import AbstractUser
from django.db.models import TextField


class User(AbstractUser):
    token = TextField(max_length=256, null=False, blank=False, default=uuid4)

    def __str__(self):
        return 'id: ' + str(self.id) + ', username: ' + self.username
