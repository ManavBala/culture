from django.contrib import admin
from .models import Quiz, Art, Answered
# Register your models here.
admin.site.register(Quiz)
admin.site.register(Art)
admin.site.register(Answered)