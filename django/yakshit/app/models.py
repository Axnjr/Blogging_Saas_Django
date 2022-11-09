from os import link
from pyexpat import model
from django.db import models
from datetime import datetime , date
import uuid
import random
ist = datetime.now()
n = random.randint(0,3)

class Videos(models.Model):
    link_to_vid = models.URLField(max_length=10000,blank=True,null=True)
    def __str__(self) -> str:
        return self.link_to_vid

class Categories(models.Model):
    name = models.TextField(max_length=40,default='first')
    def __str__(self):
        return self.name

class WatchLater(models.Model):
    link_to_vid = models.URLField(max_length=10000,blank=True,null=True)
    def __str__(self) -> str:
        return self.link_to_vid
    
class LikedVideos(models.Model):
    link_to_vid = models.URLField(max_length=10000,blank=True,null=True)       
    def __str__(self) -> str:
        return self.link_to_vid

class Subscriptions(models.Model):
    Chanel_Name = models.CharField(max_length=100,blank=True,null=True)
    def __str__(self) -> str:
        return self.Chanel_Name


