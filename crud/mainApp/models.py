from django.db import models

# Create your models here.

class Employee(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    phone = models.CharField(max_length=11)
    dsg = models.CharField(max_length=50)
    salary = models.IntegerField()
    city = models.CharField(max_length=50,null=True,default="")
    state = models.CharField(max_length=50,null=True,default="")


    def __str__(self):
        return str(self.id)+" "+self.name+" "+self.email
