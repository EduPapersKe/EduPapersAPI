from rest_framework import serializers

from .models import User, Developer, APIKey

#pylint: disable=no-member
class UserSerializer(serializers.ModelSerializer):
    email = serializers.CharField()
    username = serializers.CharField(max_length=12)
    password = serializers.CharField(write_only=True)
    
    def validate_email(self, value): # Check if the email is already in use.
        if User.objects.filter(email=value).exists():
            raise serializers.ValidationError("This email is already in use.")
        return value

    def validate_username(self, value): # Check if the username is already in use.
        if User.objects.filter(username=value).exists():
            raise serializers.ValidationError("This username is already in use.")
        return value
    
    def create(self, validated_data):
        user = User.objects.create(
            email = validated_data['email'],
            username = validated_data['username'],
        )
        user.set_password(validated_data['password'])
        user.save()
        return user
    
    class Meta:
        model = User
        fields = ["id", "email", "username", "password"]
        
        
class DeveloperSerializer(serializers.ModelSerializer):
    email = serializers.CharField()
    first_name = serializers.CharField(max_length=10)
    last_name = serializers.CharField(max_length=10)
    
    def validate_email(self, value): # Check if the email is already in use.
        if Developer.objects.filter(email=value).exists():
            raise serializers.ValidationError("This email is already in use.")
        return value
    
    def create(self, validated_data):
        developer = Developer.objects.create(
            email = validated_data['email'],
            first_name = validated_data['first_name'],
            last_name = validated_data['last_name'],
        )
        developer.save()
        return developer
    
    class Meta:
        model = Developer
        fields = ["id", "email", "first_name", "last_name"]
        
    
class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(write_only=True)
    

class APIKeySerializer(serializers.ModelSerializer):
    owner = serializers.PrimaryKeyRelatedField(read_only=True)
    api_key = serializers.UUIDField(read_only=True)

    class Meta:
        model = APIKey
        fields = ['owner', 'api_key']