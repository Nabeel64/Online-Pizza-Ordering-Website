from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models.deletion import CASCADE

class User(AbstractUser):
    userpic = models.ImageField(upload_to="profliepics/", default="achari_do_pyaza.jpg")

class Pizzas(models.Model):
    y=[('NV','Non-Veg'),('VG','Veg')]
    pname=models.CharField(max_length=50)
    pregular=models.IntegerField()
    pmedium=models.IntegerField()
    plarge=models.IntegerField()
    pcategory = models.CharField(choices=y,default="NV",max_length=12)
    pimage=models.ImageField(upload_to="pizzaimages/",default="achari_do_pyaza.jpg")

class Cart(models.Model):
    pname=models.CharField(max_length=50)
    psize=models.CharField(max_length=50)
    pcost=models.IntegerField()
    uid=models.ForeignKey(User,on_delete=models.CASCADE,null=True)
# Create your models here.

class Order(models.Model):
    uname=models.CharField(max_length=50)
    mnumb=models.CharField(max_length=10)
    pizzas=models.CharField(max_length=100000)
    tcost=models.IntegerField()
    address=models.CharField(max_length=500)

class Orderhistory(models.Model):
    pizzas=models.CharField(max_length=100000)
    tcost=models.IntegerField()
    address=models.CharField(max_length=500)
    time=models.DateTimeField(null=True,auto_now=True)
    uid=models.ForeignKey(User,on_delete=models.CASCADE,null=True)