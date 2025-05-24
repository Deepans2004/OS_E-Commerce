from django.db import models
from django.contrib.auth.models import User
from datetime import date
import datetime




#product model
class Product(models.Model):
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='products/')
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name
    



#shipping 
class WishlistItem(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    def total_price(self):
        return self.product.price * self.quantity

    def __str__(self):
        return f"{self.user.username} - {self.product.name} ({self.quantity})"



#model for Profile
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
    



