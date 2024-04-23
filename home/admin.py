from django.contrib import admin
from .models import listing, Seller, Buyer
# Register your models here.
admin.site.register(Seller)
admin.site.register(Buyer)
admin.site.register(listing)
