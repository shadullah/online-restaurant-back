from django.db import models
from users.models import User
from restaurants.models import Menu, Restaurant

# Create your models here.
class Cart(models.Model):
    quantity = models.PositiveIntegerField(default=1)
    price= models.DecimalField(max_digits=8, decimal_places=2)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    items = models.ForeignKey(Menu, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user} {self.items.name}"
    
class Order(models.Model):
    STATUS_CHOICES =(
        ('pending', 'Pending'), 
        ('confirmed', 'Confirmed'),
        ('preparing', 'Preparing'),
        ('out_for_delivery', 'Out for Delivery'),
        ('delivered', 'Delivered'),
        ('cancelled', 'Cancelled'),
    )

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    total_amount = models.DecimalField(max_digits=8, decimal_places=2)
    delivery_address = models.TextField()

    def __str__(self):
        return f"Order of {self.user.email}"
    
class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    menu_item = models.ForeignKey(Menu, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    price= models.DecimalField(max_digits=8, decimal_places=2)

    def __str__(self):
        return f"{self.menu_item.name} {self.order.id}"
