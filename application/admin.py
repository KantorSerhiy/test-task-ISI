from django.contrib import admin

from application.models import User, Message, Thread

admin.site.register(User)
admin.site.register(Message)
admin.site.register(Thread)
