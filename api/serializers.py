from datetime import timezone
from rest_framework import serializers


from .models import Resource, Tag ,Comment


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ['id', 'tag_name'] 
        
        
class ResourceSerializer(serializers.ModelSerializer):
    title = serializers.CharField(max_length=100)
    description = serializers.CharField(allow_blank=True, max_length=None)
    publisher = serializers.StringRelatedField(read_only=True)
    tags = TagSerializer(many=True, required=False)
    file = serializers.FileField(required=True)
    date_created = serializers.DateTimeField(format="%B  %d, %Y, %I:%M %p")
    
    class Meta:
        model = Resource
        fields = ['id', 'title', 'description', 'publisher', 'tags', 'date_created', 'file', 'file_size', 'file_format']


class CommentSerializer(serializers.ModelSerializer):
    author = serializers.StringRelatedField(read_only=True)
    date_created = serializers.DateTimeField(format="%B %d, %Y, %I:%M %p",read_only=True)
    
    class Meta:
        model = Comment
        fields = ['id', 'resource', 'author', 'text', 'date_created']
    