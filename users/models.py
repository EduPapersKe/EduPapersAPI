import uuid
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin


#pylint: disable=no-member
class UserManager(BaseUserManager):
    def create_user(self, email, username, password=None):
        user = self.model(
            email = self.normalize_email(email),
            username = username,
            password = password,
        )
        user.set_password(password)
        user.save(using=self._db)
        return user
        
    
    def create_superuser(self, email, username, password=None):
        user = self.create_user(
            email = self.normalize_email(email),
            username = username,
            password = password,
        )
        user.is_admin = True
        user.is_superuser = True
        user.is_staff = True
        user.is_active = True
        
        user.set_password(password)
        user.save(using=self._db)
        return user
        

class User(AbstractBaseUser, PermissionsMixin):
    """
    This type of user is the regular platform user who logs in and interacts with the application.
    """
    id = models.UUIDField(primary_key=True, unique=True, default=uuid.uuid4, editable=False)
    email = models.EmailField(unique=True, null=True, blank=False)
    username = models.CharField(max_length=12, unique=True, null=True, blank=False)
    is_verified = models.BooleanField(default=False)
    
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']
    
    objects = UserManager()
    
    def save(self, *args, **kwargs):
        self.email = self.email.lower()
        self.username = self.username.lower()
        super().save(*args, **kwargs)
    
    def has_module_perms(self, app_label):
        return True
        
    def __str__(self):
        return f"{self.username}"
    
    
class Developer(models.Model):
    """
    This type of user cannot log in. They are just represented by this model which is referenced in the APIKey model.
    This type of user is the client application developer authorised to call the API endpoints.
    """
    id = models.UUIDField(primary_key=True, unique=True, editable=False)
    email = models.EmailField(unique=True, null=True)
    first_name = models.CharField(max_length=10, null=True)
    last_name = models.CharField(max_length=10, null=True)
    description = models.CharField(max_length=200, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='developers_created')
    
    def save(self, *args, **kwargs):
        self.email = self.email.lower()
        super().save(*args, **kwargs)
    
    def __str__(self):
        return f"{self.email}"
    
    
class APIKey(models.Model):
    """
    This model stores the API keys generated for each Developer authorised to build on the API.
    """
    owner = models.ForeignKey(Developer, on_delete=models.CASCADE, null=False, blank=False)
    api_key = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.owner.email}"