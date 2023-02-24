from rest_framework import generics, status, exceptions

from rest_framework.generics import CreateAPIView, ListAPIView

from rest_framework.permissions import IsAdminUser

from django.db.models import Count
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Thread, Message, User
from .serializers import ThreadSerializer, MessageSerializer


class CreateThreadAPIView(CreateAPIView):
    queryset = Thread.objects.all()
    serializer_class = ThreadSerializer

    def create(self, request, *args, **kwargs):
        participants = request.data.get("participants")

        if participants is None:
            return Response(
                {"participants": ["This field is required."]},
                status=status.HTTP_400_BAD_REQUEST,
            )

        users = request.data
        users_dict = dict(users)["participants"]
        if len(users_dict) != 2:
            return Response(
                {"participants": ["Only two participants are allowed."]},
                status=status.HTTP_400_BAD_REQUEST,
            )

        return super().create(request, *args, **kwargs)

    def perform_create(self, serializer):
        participants = serializer.validated_data.get("participants")
        # check if thread with these participants already exists
        thread = (
            Thread.objects.filter(participants__in=participants)
            .distinct()
            .annotate(count=Count("participants"))
            .filter(count=len(participants))
        )
        if thread.exists():
            serializer.instance = thread.first()
        else:
            serializer.save()


class ThreadDeleteAPIView(generics.DestroyAPIView):
    serializer_class = ThreadSerializer
    permission_classes = [
        IsAdminUser,
    ]

    def get_queryset(self):
        user = self.request.user
        queryset = Thread.objects.filter(participants=user)
        return queryset


class ThreadListAPIView(generics.ListAPIView):
    serializer_class = ThreadSerializer

    def get_queryset(self):
        user = self.request.user
        queryset = Thread.objects.filter(participants=user)
        return queryset


class MessageListAPIView(ListAPIView):
    serializer_class = MessageSerializer

    def get_queryset(self):
        thread_id = self.kwargs["thread_id"]
        return Message.objects.filter(thread_id=thread_id).select_related("sender")


class CreateMessageAPIView(CreateAPIView):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer

    def create(self, request, *args, **kwargs):
        thread_id = request.data.get("thread")

        thread = Thread.objects.filter(id=thread_id, participants=request.user).first()

        if thread is None:
            return Response(
                {"error": "You cannot post messages to this thread."},
                status=status.HTTP_403_FORBIDDEN,
            )

        return super().create(request, *args, **kwargs)

    def perform_create(self, serializer):
        return serializer.save(sender=self.request.user)


class MessageReadAPIView(APIView):
    def post(self, request, thread_id):
        Message.objects.filter(thread_id=thread_id, is_read=False).update(is_read=True)
        return Response(
            {"messages": [f"All messages in thread {thread_id} read!"]},
            status=status.HTTP_200_OK,
        )


class UnreadMessageCountAPIView(APIView):
    def get(self, request):
        count = Message.objects.filter(
            thread__participants=request.user, is_read=False
        ).count()
        return Response({"count": count})
