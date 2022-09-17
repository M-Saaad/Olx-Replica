from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class UserSignup(models.Model):
    UserID = models.AutoField(primary_key=True)
    UserFirstName = models.CharField(max_length=500)
    UserLastName = models.CharField(max_length=500)
    UserContactNo = models.CharField(max_length=500)
    UserEmail = models.CharField(max_length=500)
    UserPassword = models.CharField(max_length=500)

class UserLogin(models.Model):
    UserEmail = models.CharField(max_length=500)
    UserPassword = models.CharField(max_length=500)

class UserDetail(models.Model):
    UserEmail = models.CharField(max_length=500)
    UserFirstName = models.CharField(max_length=500)
    UserLastName = models.CharField(max_length=500)
    UserContactNo = models.CharField(max_length=500)

class Laptops(models.Model):
    UserEmail = models.CharField(max_length=500)
    LaptopId = models.AutoField(primary_key=True)
    LaptopName = models.CharField(max_length=500)
    LaptopImage = models.CharField(max_length=500)
    LaptopScreenSize = models.FloatField()
    LaptopScreenResolution = models.FloatField()
    LaptopRam = models.FloatField()
    LaptopHDD = models.FloatField()
    LaptopSSD = models.FloatField()
    LaptopDetails = models.CharField(max_length=1000)
    LaptopPrice = models.FloatField()

class Mobiles(models.Model):
    UserEmail = models.CharField(max_length=500)
    MobileId = models.AutoField(primary_key=True)
    MobileName = models.CharField(max_length=500)
    MobileImage = models.CharField(max_length=500)
    MobileRom = models.CharField(max_length=500)
    MobileScreen = models.FloatField()
    MobilePrimaryCam = models.FloatField()
    MobileSalfieCam = models.FloatField()
    MobileBattery = models.FloatField()
    MobileDetails = models.CharField(max_length=1000)
    MobilePrice = models.FloatField()