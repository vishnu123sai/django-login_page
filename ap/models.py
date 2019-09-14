from django.db import models

# Create your models here.
class UserDetails(models.Model):
    first_name = models.CharField(max_length=20);
    last_name = models.CharField(max_length=20);
    email =  models.CharField(max_length=20);
    password = models.CharField(max_length=15);
