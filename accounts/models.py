from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField
# Create your models here.
class Poem(models.Model):
    title = models.CharField(max_length=255)
    body = RichTextField()
    author =models.ForeignKey(User,  on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.title

    
   