from django.db import models
# Create your models here.
class visitors(models.Model):
    name=models.CharField(max_length=100)
    phonenumber=models.IntegerField()
    address=models.CharField(max_length=500)
    email=models.EmailField()
    password=models.CharField(max_length=100)
    confirmpassword=models.CharField(max_length=100)

class contactus(models.Model):
    name=models.CharField(max_length=100)
    email=models.EmailField()
    subject=models.CharField(max_length=200)
    messages=models.TextField()

class depadmin(models.Model):
    tittle=models.CharField(max_length=200)
    shortdec=models.CharField(max_length=200)
    detaileddec=models.TextField()
    dec=models.TextField(null=True)

