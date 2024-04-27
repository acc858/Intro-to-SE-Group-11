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
    
class Purchase(models.Model):
    buyer = models.ForeignKey(Buyer, on_delete=models.CASCADE)
    listing = models.ForeignKey(listing, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    price = models.IntegerField()

    purchase_date = models.DateTimeField(auto_now_add=True)

    def str(self):
        return f"{self.buyer.username}'s Purchase(s) of {self.listing.title}"

class Notification(models.Model):
    seller=models.ForeignKey(Seller, on_delete=models.CASCADE)
    buyer=models.ForeignKey(Buyer, on_delete=models.CASCADE)
    listing=models.ForeignKey(listing, on_delete=models.CASCADE)
    price=models.IntegerField()
    quantity=models.IntegerField()

    def str(self):
        return f"{self.buyer.username} has purchased {self.seller.username}'s {self.listing.title} for ${self.listing.price}"

class Return_Notification(models.Model):
    seller=models.ForeignKey(Seller, on_delete=models.CASCADE)
    buyer=models.ForeignKey(Buyer, on_delete=models.CASCADE)
    listing=models.ForeignKey(listing, on_delete=models.CASCADE)
    price=models.IntegerField()
    quantity=models.IntegerField()

    def str(self):
        return f"{self.buyer.username} has returned {self.seller.username}'s {self.listing.title} for ${self.listing.price}"
    
class Admin(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    email= models.TextField()
    username= models.TextField()

    def str(self):
        return self.email