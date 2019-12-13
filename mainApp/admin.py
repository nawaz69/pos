from django.contrib import admin
from .models import Order,Product,Customers,Order_Detail,Order_Rough

# Register your models here.
admin.site.register(Product)
admin.site.register(Order)
admin.site.register(Customers)
admin.site.register(Order_Rough)
admin.site.register(Order_Detail)




