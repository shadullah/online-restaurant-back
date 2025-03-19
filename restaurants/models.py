from django.db import models
from users.models import User

# Create your models here.
class Restaurant(models.Model):
    name=models.CharField(max_length=500)
    description = models.TextField()
    location = models.CharField(max_length=800)
    image = models.ImageField(upload_to='images', blank=True, null=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
    
class Menu(models.Model):
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='images', blank=True, null=True)
    name=models.CharField(max_length=500)
    description = models.TextField()
    price=models.DecimalField(max_digits=8, decimal_places=2)
    is_available = models.BooleanField(default=True)

    def __str__(self):
        return self.name
