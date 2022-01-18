from django.db import models
from django.db.models.deletion import CASCADE
from django.dispatch import receiver
from django.db.models.signals import post_delete

# Create your models here.
class Course(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=50)
    details = models.TextField()
    def __str__(self):
        return self.title

class Result(models.Model):
    id = models.AutoField(primary_key=True)
    med_choices = (('Marathi','Marathi'),('SemiEng','SemiEng'),('Foundation','Foundation'))
    sub_choices = (('Mathematics','Mathematics'),('English','English'),('Science','Science'))
    std_choices = ((1,1),(2,2),(3,3),(4,4),(5,5),(6,6),(7,7),(8,8),(9,9),(10,10))
    title = models.CharField(max_length=50)
    link = models.CharField(max_length=500)
    sub = models.CharField(max_length=15,choices=sub_choices)
    std = models.IntegerField(choices=std_choices)
    medium = models.CharField(max_length=10,choices=med_choices)
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.title

class Notification(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=50)
    description = models.TextField()
    def __str__(self):
        return self.title

class Guest(models.Model):
    name = models.CharField(max_length=20)
    email = models.CharField(max_length=30)
    sub = models.CharField(max_length=20)
    message = models.TextField()
    def __str__(self):
        return self.name

