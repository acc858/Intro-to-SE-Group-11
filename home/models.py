from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Seller(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    email = models.EmailField()
    username = models.CharField(max_length=150)
    balance = models.DecimalField(max_digits=10, decimal_places=2,null=True)
    def __str__(self):
        return self.email
    
class Buyer(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    email = models.TextField()
    username = models.TextField()
    def __str__(self):
        return self.email
    
class listing(models.Model):
    title=models.CharField(max_length=200)
    author=models.CharField(max_length=200)
    year=models.IntegerField()
    quantity=models.IntegerField()
    isbn=models.IntegerField()
    price=models.IntegerField()
    seller=models.ForeignKey(Seller, on_delete=models.CASCADE)
    image=models.CharField(max_length=200)
    

    def __str__(self):
        return self.title