from django.db import models
from django.db.models.fields import Field
from django.forms.widgets import RadioSelect
from django.contrib.auth.models import AbstractUser

# class User(AbstractUser):
#     email = models.EmailField(verbose_name='email',max_length=255,unique=True)
#     phone = models.CharField(null=True, max_length=50)
#     REQUIRED_FIELDS = ['email','phone','first_name','last_name']
#     USERNAME_FIELD = 'username'
#     def get_username(self):
#         return self.username

# Create your models here.

class Photo(models.Model):
    id = models.IntegerField(primary_key=True,null=False,unique=True)
    userid = models.IntegerField(null=False)
    username = models.CharField(null=False, max_length=50)
    photo_name = models.ImageField(null=False)
    reyting = models.IntegerField(null=False)
    shows = models.IntegerField(null=False)
    performance = models.IntegerField(null=False)
    yt = models.DateTimeField(auto_now_add=True)


class Photo2(models.Model):
    id = models.BigAutoField(primary_key=True,null=False,unique=True)
    username = models.CharField(null=False, max_length=50)
    photo_name1 = models.ImageField()
    photo_name2 = models.ImageField()
    reyting = models.IntegerField(null=False)
    reyting2 = models.IntegerField(null=False)
    shows = models.IntegerField(null=False)
    yt = models.DateTimeField(auto_now_add=True)
    role=[(0,'herkes'),
        (1,'gizli')]
    hide = models.IntegerField(null=False,choices=role,default=0)

class ppUser(models.Model):
    id = models.BigAutoField(primary_key=True,null=False,unique=True)
    username = models.CharField(null=False, unique=True, max_length=50)
    pp = models.ImageField()

    
class followEvent(models.Model):
    id = models.BigAutoField(primary_key=True,null=False,unique=True)
    following = models.CharField(null=False, max_length=50)
    followed = models.CharField(null=False, max_length=50) 
    photo_true = models.IntegerField(null=False)
    photo_true2 = models.IntegerField(null=False)


class viewing2(models.Model):
    id = models.BigAutoField(primary_key=True,null=False,unique=True)
    following = models.CharField(null=False, max_length=50)
    followed = models.CharField(null=False, max_length=50) 
    photo_name = models.CharField(null=False, max_length=500)
    photo_name2 = models.CharField(null=False, max_length=500)
    view = models.IntegerField(null=False)

class feedback(models.Model):
    id = models.BigAutoField(primary_key=True,null=False,unique=True)
    complaining = models.CharField(null=False, max_length=50)
    complained = models.CharField(null=False, max_length=50)
    photo_name = models.CharField(null=True, max_length=500,unique=True)
    photo_name2 = models.CharField(null=True, max_length=500,unique=True)


class photoLiked(models.Model):
    id = models.BigAutoField(primary_key=True,null=False,unique=True)
    username = models.CharField(null=False, max_length=50)
    photo_name = models.CharField(null=True, max_length=500)


class photoLiked2(models.Model):
    id = models.BigAutoField(primary_key=True,null=False,unique=True)
    username = models.CharField(null=False, max_length=50)
    photo_name1 = models.CharField(null=True, max_length=500)
    photo_name2 = models.CharField(null=True, max_length=500)


class photoBlock(models.Model):
    id = models.BigAutoField(primary_key=True,null=False,unique=True)
    username = models.CharField(null=False, max_length=50)
    photo_name = models.CharField(null=True, max_length=500)


class photoBlock2(models.Model):
    id = models.BigAutoField(primary_key=True,null=False,unique=True)
    username = models.CharField(null=False, max_length=50)
    photo_name1 = models.CharField(null=True, max_length=500)
    photo_name2 = models.CharField(null=True, max_length=500)


class photoSave(models.Model):
    id = models.BigAutoField(primary_key=True,null=False,unique=True)
    username = models.CharField(null=False, max_length=50)
    photo_name = models.CharField(null=True, max_length=500)
