from django.db import models
from django.contrib.auth.models import User
import datetime 
from datetime import date  # ✅ Add this line

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    age = models.IntegerField()
    phone = models.CharField(max_length=15)
    
    def default_dob():
        return date(1999, 1, 1)

    dob = models.DateField(default=default_dob, null=False, blank=False)
    address = models.TextField()

    def __str__(self):
        return f"{self.user.username}'s profile"
