from django.contrib import admin
from .models import listing, Seller, Buyer, Purchase, Notification, Return_Notification
# Register your models here.
admin.site.register(Seller)
admin.site.register(Buyer)
admin.site.register(listing)
admin.site.register(Purchase)
admin.site.register(Notification)
admin.site.register(Return_Notification)