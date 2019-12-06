from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings
from django_mysql.models import ListTextField

# Create your models here.
class CustomUser(AbstractUser):
    # add additional fields in here
    email = models.EmailField(null=True,blank=True)
    is_staff = models.BooleanField(default=True)
    user_img = models.FileField(upload_to="static/images/profiles",null=True,blank=True)

