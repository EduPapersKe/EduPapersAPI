from rest_framework import serializers

from .models import Resource, Tag


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ['id', 'tag_name'] 
        
        
class ResourceSerializer(serializers.ModelSerializer):
    title = serializers.CharField(max_length=100)
    description = serializers.CharField(allow_blank=True, max_length=None)
    publisher = serializers.PrimaryKeyRelatedField(read_only=True)
    tags = TagSerializer(many=True, required=False)
    file = serializers.FileField(required=True)
    
    class Meta:
        model = Resource
        fields = ['id', 'title', 'description', 'publisher', 'tags', 'date_created', 'file', 'file_size', 'file_format']
