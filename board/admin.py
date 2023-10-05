from django.contrib import admin

# Register your models here.

from .models import BoardMessage

admin.site.register(BoardMessage)
