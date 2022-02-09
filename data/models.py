from django.db import models


# Create your models here.
class SaleForm(models.Model):
    types = models.CharField(max_length=10)
    dist = models.CharField(max_length=30)
    thaluk = models.CharField(max_length=30)
    add = models.CharField(max_length=50)
    name = models.CharField(max_length=30)
    phone = models.CharField(max_length=10)
    email = models.EmailField()
    amt = models.IntegerField()
    desc = models.TextField()
    image = models.ImageField(upload_to="images")
    video = models.FileField(upload_to="videos")


class RentForm(models.Model):
    types = models.CharField(max_length=10)
    dist = models.CharField(max_length=30)
    thaluk = models.CharField(max_length=30)
    add = models.CharField(max_length=50)
    name = models.CharField(max_length=30)
    phone = models.CharField(max_length=10)
    email = models.EmailField()
    amt = models.IntegerField()
    bed = models.CharField(max_length=10)
    door = models.CharField(max_length=10)
    desc = models.TextField()
    image = models.ImageField(upload_to="images")
    video = models.FileField(upload_to="videos")


class Contact(models.Model):
    username = models.CharField(max_length=30)
    phone = models.CharField(max_length=10)
    email = models.EmailField()
    desc = models.TextField()
