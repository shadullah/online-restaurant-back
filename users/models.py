from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    class UserType(models.TextChoices):
        OWNER = 'Owner'
        USER = 'User'
    
    username = models.CharField(max_length=100,unique=True)
    email=models.EmailField(max_length=500, unique=True)
    address= models.CharField(max_length=800)
    image=models.ImageField(upload_to='images',blank=True, null=True)
    user_type = models.CharField(max_length=50, choices=UserType.choices, default=UserType.USER)

    first_name=None
    last_name=None

    USERNAME_FIELD="email"
    REQUIRED_FIELDS =["user_type", "username"]

    def __str__(self):
        return self.email