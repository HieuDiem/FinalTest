from django.db import models

# Create your models here.

class Students(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=30)
    age = models.IntegerField()
    address = models.CharField(max_length=100)
    mobile_number = models.CharField(max_length=11)

    def __str__(self):
        return self.name

    
class Teacher(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=30)
    age = models.IntegerField()
    address = models.CharField(max_length=100)

    def __str__(self):
        return self.name

