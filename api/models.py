from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
# Create your models here.
class Studpersonal(models.Model):
    Name = models.CharField(max_length=25)
    Age = models.CharField(max_length=3,null=True)
    Dob = models.DateField(null=True)
    Father_Name = models.CharField(max_length=25,null=True)
    Mother_Name = models.CharField(max_length=25,null=True)
    Mobile_Number = PhoneNumberField(unique = False, null = True, blank = False)#Later On I Can Provide unique no to evreyone
    Email = models.EmailField(null=True)
    Blood_Group = models.CharField(max_length=10,null=True)
    Class = models.CharField(max_length=25,null=True)
    Sec = models.CharField(max_length=25,null=True)