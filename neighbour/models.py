from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Neighbour(models.Model):
    name = models.CharField(max_length =30,null=True)
    location = models.CharField(max_length =30,null=True)
    image = models.ImageField(upload_to = 'images/',null=True)
    occupants = models.IntegerField(null=True)
    police_dept = models.IntegerField(null=True)
    health_dept = models.IntegerField(null=True)
    user = models.ForeignKey(User, null=True)
    objects = models.Manager()
    # Admin Foreign key
    def __str__(self):
        return self.name


# User class
class Profile(models.Model):
    pro_photo = models.ImageField(upload_to = 'images/',null=True)
    name = models.CharField(max_length =30,null=True)
    location = models.CharField(max_length =30,null=True)
    email = models.EmailField(max_length =50,null=True)
    neighbourhood = models.ForeignKey(Neighbour, null=True)
    bio = models.CharField(max_length =150,null=True)
    user = models.OneToOneField(User,on_delete=models.CASCADE,related_name='profile',null=True)
    
    def __str__(self):
        return self.name

class Business(models.Model):
    name = models.CharField(max_length =30,null=True)
    description = models.CharField(max_length =130,null=True)
    email = models.EmailField(max_length =50,null=True)
    user = models.ForeignKey(User, null=True)
    neighbourhood = models.ForeignKey(Neighbour, null=True)
 
    objects = models.Manager()
    def __str__(self):
        return self.name


class Post(models.Model):
    post = models.CharField(max_length =130,null=True)
    user = models.ForeignKey(User, null=True)
    neighbourhood = models.ForeignKey(Neighbour,related_name='post',null=True)

    class Meta:
        ordering = ['id']
    objects = models.Manager()
 
    def __str__(self):
        return self.post



