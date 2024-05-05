from django.contrib import admin

from .models import User, Developer, APIKey

admin.site.register(User)
admin.site.register(Developer)
admin.site.register(APIKey)