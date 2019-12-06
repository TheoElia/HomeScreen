from django.db import models
from django.conf import settings
from django_mysql.models import ListTextField


class Category(models.Model):
    # THEME_CHOICES = (
    #     ('Education', 'Education'),
    #     ('Health', 'Health'),
    #     ('Sports', 'Sports'),
    #     ('Telco','Telco'),
    #     ('Thursday','Thursday'),
    #     ('Friday','Friday'),
    #     ('Saturday','Saturday')
    # )
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name


# Create your models here.
class App(models.Model):
    name = models.CharField(max_length=250,unique=True)
    url = models.URLField(null=True,blank=True)
    date_added = models.DateTimeField(null=True,auto_now_add=True)
    categories = models.ManyToManyField(Category)
    head_img = models.FileField(upload_to="static/images/heads",null=True,blank=True)
    description = models.TextField(null=True,blank=True)
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, blank = True, on_delete = models.SET_NULL)

    def __str__(self):
        return self.name

# Migrate App before this model
class AppImage(models.Model):
    app = models.ForeignKey(App,null=True,on_delete = models.SET_NULL, related_name='images')
    image = models.FileField(upload_to="static/apps/images",null=True)
    time = models.DateTimeField(null=True,auto_now_add=True)


class Rate(models.Model):
    rating = models.IntegerField(default=0.0)
    review = models.TextField(null=True)
    app = models.ForeignKey(App, null=True, blank = True, on_delete = models.SET_NULL)
    date_time = models.DateTimeField(null=True,blank=True,auto_now_add=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, blank = True, on_delete = models.SET_NULL)

    def __str__(self):
        return str(self.rating)

class Update(models.Model):
    app = models.ForeignKey(App, null=True, blank = True, on_delete = models.SET_NULL)
    features = ListTextField(base_field=models.CharField(max_length=1000),size=5000,blank=True,null=True)
    date_time = models.DateTimeField(null=True,blank=True,auto_now_add=True)