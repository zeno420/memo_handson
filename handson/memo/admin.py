from django.contrib import admin

from .models import Memo, Attachment

admin.site.register(Memo)
admin.site.register(Attachment)
