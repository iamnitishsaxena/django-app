from django.db import models

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=1000)
    text = models.TextField()

class Comment(models.Model):
    name = models.CharField(max_length = 1000)
    comment = models.TextField()
    post_id = models.IntegerField(default =0)
