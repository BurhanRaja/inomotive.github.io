# Create your models here.
from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import now

class Post(models.Model):
    sno = models.AutoField(primary_key=True)
    title = models.CharField(max_length=255)
    content = models.TextField(blank=True, null=True)
    author = models.CharField(max_length=30)
    slug = models.CharField(max_length=130)
    views= models.IntegerField(default=0)
    timeStamp = models.DateTimeField(blank=True)
    image = models.ImageField(upload_to= "static/images", default="")

    def __str__(self):
        return self.title + ' by ' + self.author


class BlogComment(models.Model):
    sno = models.AutoField(primary_key=True)
    comment = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True)
    timeStamp = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.comment[0:13] + "..." + "by" + self.user.first_name
    

