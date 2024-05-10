import uuid
from django.db import models

from users.models import User

#pylint: disable=no-member
def resource_path(instance, filename):
    return f"resources/{instance.id}/{filename}" # Generate the upload path for resources


class Category(models.Model):
    name = models.CharField(max_length=50, null=True)
    
    class Meta:
        verbose_name_plural = 'Categories'
        
    def __str__(self):
        return f"{self.name}"
    
    
class Tag(models.Model):
    """
    For a list of the tags in the database, refer to https://github.com/EduPapersKe/EduPapersAPI/blob/master/tags.txt
    """
    id = models.AutoField(primary_key=True, unique=True, editable=False)
    tag_name = models.CharField(max_length=20, null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True)
    
    def save(self, *args, **kwargs):
        self.tag_name = self.tag_name.lower()
        super().save(*args, **kwargs)
    
    def __str__(self):
        return f"{self.tag_name}"
    
class Resource(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=100, null=True, blank=False)
    description = models.TextField(null=True, blank=False)
    publisher = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    date_created = models.DateTimeField(auto_now_add=True)
    file = models.FileField(upload_to=resource_path, null=True, blank=False)
    file_size = models.IntegerField(null=True)
    """
    The tags related to a resource. A resource can have multiple tags or none.
    """
    tags = models.ManyToManyField(Tag, blank=True)
    file_format = models.CharField(max_length=7, null=True) # PDF, DOCX, xlsx, CSV, ODS, ZIP, TXT, EPUB, MOBI, AZW only
    
    def __str__(self):
        return f"{self.title}"
    
    
class Comment(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    resource = models.ForeignKey(Resource, on_delete=models.CASCADE)
    text = models.CharField(max_length=100, null=True, blank=False)
    date_created = models.DateTimeField(auto_now_add=True)

    @staticmethod
    def can_comment(request,resource):
        """
        this func helps to ensure that a user can only comment on a single resource only Once. this prevents
        the comment section from becomming a kind of chatroom where a user keep sending messages on one resource.
        additionally this feature prevents a potential Dos attack where user might flood the comment section with messages 
        slowing down the server.its not nessesary but can be called **Comment.can_comment()**if needed to limit comments per user.
        """
        comments = Comment.objects.filter(resource=resource,author=request.user)
        if len(comments )< 1 :
            return True
        elif len(comments)>1:
            return False
    
    def __str__(self):
        return f"{self.text}"