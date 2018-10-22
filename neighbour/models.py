from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Neighbour(models.Model):
    name = models.CharField(max_length =30,null=True)
    location = models.CharField(max_length =30,null=True)
    image = models.ImageField(upload_to = 'images/',null=True)
    occupants = models.IntegerField(null=True)
    user = models.ForeignKey(User, null=True)
    # Admin Foreign key


# User class
class Profile(models.Model):
    pro_photo = models.ImageField(upload_to = 'images/',null=True)
    name = models.CharField(max_length =30,null=True)
    email = models.EmailField(max_length =50,null=True)
    neighbourhood = models.ForeignKey(Neighbour, null=True)
    user = models.OneToOneField(User,on_delete=models.CASCADE,related_name='profile',null=True)


class Business(models.Model):
    name = models.CharField(max_length =30,null=True)
    email = models.EmailField(max_length =50,null=True)
    user = models.ForeignKey(User, null=True)
    neighbourhood = models.ForeignKey(Neighbour, null=True)




