from django.contrib import admin

from .models import Resource, Tag, Comment, Category

admin.site.register(Resource)
admin.site.register(Tag)
admin.site.register(Comment)
admin.site.register(Category)