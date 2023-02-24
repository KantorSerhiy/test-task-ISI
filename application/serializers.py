from rest_framework import serializers
from .models import Thread, Message, User

from rest_framework import serializers
from .models import Thread, Message


class MessageSerializer(serializers.ModelSerializer):
    sender = serializers.StringRelatedField()

    class Meta:
        model = Message
        fields = ["sender", "thread", "text", "created"]


class ThreadSerializer(serializers.ModelSerializer):
    participants = serializers.SlugRelatedField(
        many=True, queryset=User.objects.all(), slug_field="username"
    )
    last_message = serializers.SerializerMethodField()

    def get_last_message(self, obj):
        message = obj.messages.last()
        if message:
            return MessageSerializer(message).data["text"]

    class Meta:
        model = Thread
        fields = "__all__"
