from django.db import models
from django.contrib.auth.models import User
from datetime import date
import datetime



class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    age = models.IntegerField(default=0)
    phone = models.CharField(max_length=15, null=True)
    address = models.TextField(null=True)
    def default_dob():
        return datetime.date(2000, 1, 1)

    dob = models.DateField(default=default_dob)

    def __str__(self):
        return f"{self.user.username}'s profile"
