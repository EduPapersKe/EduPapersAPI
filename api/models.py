import uuid
from django.db import models

from users.models import User

#pylint: disable=no-member
class Resource(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=100, null=True, blank=False)
    description = models.TextField(null=True, blank=False)
    publisher = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    date_created = models.DateTimeField(auto_now_add=True)
    file_size = models.IntegerField(null=True)
    """
    Here comes the tags related to a resource. A resource will have multiple tags.
    A tags will  be in multiple resources as well.
    """
    # tags = models.ManyToManyField('Tag')
    """
    In this field, we will only allow these file formats: PDF, DOCX, xlsx, CSV, ODS, ZIP,TXT,
    EPUB, MOBI, AZW(E-books)
    """
    file_format = models.CharField(max_length=7, null=True)
    
    def __str__(self):
        return self.title + " "+ self.publisher 