from django.contrib import admin
from .models import listing, Seller, Buyer, Purchase
# Register your models here.
admin.site.register(Seller)
admin.site.register(Buyer)
admin.site.register(listing)
admin.site.register(Purchase)
