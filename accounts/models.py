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


    

class Comment(models.Model):
    poem = models.ForeignKey(Poem,  on_delete = models.CASCADE)
    body = models.TextField(max_length=255)
    author = models.ForeignKey(User,  on_delete = models.CASCADE)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.body}'