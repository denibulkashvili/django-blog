from django.db import models

from ckeditor_uploader.fields import RichTextUploadingField

# Create your models here.
class Post(models.Model):
    """Class representing posts"""
    title = models.CharField(max_length=200)
    text = RichTextUploadingField()
    date_published = models.DateTimeField('date published')
    topic = models.ForeignKey('Topic', on_delete=models.CASCADE)

    def __str__(self):
        return self.title

class Topic(models.Model):
    """Class representing topics"""
    title = models.CharField(max_length=200)

    def __str__(self):
        return self.title
    


