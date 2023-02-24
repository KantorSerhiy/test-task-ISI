from django.urls import path

from application.views import CreateThreadAPIView, ThreadDeleteAPIView, ThreadListAPIView, MessageListAPIView,\
    CreateMessageAPIView, MessageReadAPIView, UnreadMessageCountAPIView


urlpatterns = [
    path("threads/create/", CreateThreadAPIView.as_view(), name="thread-create"),
    path("threads/<int:pk>/delete/", ThreadDeleteAPIView.as_view(), name="thread-delete"),
    path("threads/", ThreadListAPIView.as_view(), name="thread-list"),
    path('threads/<int:thread_id>/messages/', MessageListAPIView.as_view(), name='message-list'),
    path('threads/message/create/', CreateMessageAPIView.as_view(), name='message-create'),
    path('threads/<int:thread_id>/messages/read/', MessageReadAPIView.as_view(), name='message-read'),
    path('unread/', UnreadMessageCountAPIView.as_view(), name='unread-count'),


]

app_name = "application"
