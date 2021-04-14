from django.db import models
# Create your models here.
# Database == Excel Workbook
# Table == sheet

class Contact(models.Model):
    sno = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    email = models.CharField(max_length=13)
    phone = models.CharField(max_length=100)
    age = models.CharField(max_length=255)
    more = models.TextField()
    timeStamp = models.DateTimeField(auto_now_add=True, blank=True)
    image = models.ImageField(upload_to= "static/images", default ="")

    def __str__(self):
        return self.name
    

   
    





