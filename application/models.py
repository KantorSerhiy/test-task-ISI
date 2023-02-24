from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    pass


class Thread(models.Model):
    participants = models.ManyToManyField(to=User, related_name="threads")
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Thread {self.id}"


class Message(models.Model):
    sender = models.ForeignKey(to=User, on_delete=models.CASCADE)
    text = models.TextField()
    thread = models.ForeignKey(
        to=Thread, on_delete=models.CASCADE, related_name="messages"
    )
    created = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField(default=False)

    def __str__(self):
        return f"Message {self.id}, Sender {self.sender}"
