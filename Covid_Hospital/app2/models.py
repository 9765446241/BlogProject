from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Doctors(models.Model):
    #id=models.IntegerField()
    name=models.CharField(max_length=50)
    address=models.CharField(max_length=100)
    @property
    def get_name(self):
        return self.user.Firstname,'',self.user.last_name
    @property
    def get_id(self):
        return self.user.id

    def __str__(self):
        return "{} ({})".format(self.user.first_name,self.department)
