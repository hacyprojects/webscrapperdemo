from django.db import models

# Create your models here.
class links(models.Model):

    address=models.CharField(max_length=500,null=True,blank=True)
    stringname=models.CharField(max_length=500,null=True,blank=True)