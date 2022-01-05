from django.db import models

# Create your models here.
class Courses(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=50)
    details = models.TextField()

class Result(models.Model):
    std_choices = ((1,1),(2,2),(3,3),(4,4),(5,5),(6,6),(7,7),(8,8),(9,9),(10,10))
    title = models.CharField(max_length=50)
    file = models.FileField(upload_to='kagne/results/')
    std = models.CharField(max_length=10,choices=std_choices)
    medium = models.CharField(max_length=15 ,choices=Courses.title)
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.CharField(max_length=512)