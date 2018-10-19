from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Neighbour(models.Model):
    name = models.CharField(max_length =30,null=True)
    location = models.CharField(max_length =30,null=True)
    occupants = models.IntegerField(null=True)
    user = models.ForeignKey(User, null=True)
    # Admin Foreign key


# User class
class Profile(models.Model):
    name = models.CharField(max_length =30,null=True)
    email = models.EmailField(max_length =50,null=True)
    neighbourhood = models.ForeignKey(Neighbour, null=True)


class Business(models.Model):
    name = models.CharField(max_length =30,null=True)
    email = models.EmailField(max_length =50,null=True)
    user = models.ForeignKey(User, null=True)
    neighbourhood = models.ForeignKey(Neighbour, null=True)




