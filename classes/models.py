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
    std_choices = ((1,1),(2,2),(3,3),(4,4),(5,5),(6,6),(7,7),(8,8),(9,9),(10,10))
    title = models.CharField(max_length=50)
    file = models.FileField(upload_to='classes/results/')
    std = models.IntegerField(choices=std_choices)
    medium = models.ForeignKey(Course,on_delete=models.CASCADE)
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


@receiver(post_delete, sender=Result)
def post_del_result(sender, instance, *args, **kwargs):
    try:
        instance.file.delete()
    except:
        pass
    
