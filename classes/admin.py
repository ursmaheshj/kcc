from django.contrib import admin
from .models import Course, Guest, Notification, Result

# Register your models here.
admin.site.register(Course)
admin.site.register(Result)
admin.site.register(Notification)
admin.site.register(Guest)
