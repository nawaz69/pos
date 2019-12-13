from django.db import models
from django.contrib.auth.models import User

# Create your models here.



class Product(models.Model):

    name=models.CharField(max_length=100)
    price=models.IntegerField()
    availability=models.BooleanField(default=True)
    date=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Customers(models.Model):
    name=models.CharField(max_length=100)
    age=models.CharField(max_length=3)
    phone_number=models.CharField(max_length=20)




class Order(models.Model):
   
    paid=models.BooleanField(default=False)
    table=models.CharField(max_length=100)
    customer=models.ForeignKey(Customers,on_delete=models.CASCADE,default=None)
    actual_price=models.IntegerField()
    discounted_price=models.IntegerField()
    grand_total=models.IntegerField()
    date=models.DateTimeField(auto_now_add=True)
    taken_by=models.ForeignKey(User,on_delete=models.CASCADE,default=None)

    def __str__(self):
        return self.table

class Order_Detail(models.Model):

        order=models.ForeignKey(Order,on_delete=models.CASCADE,default=None)
        product=models.ForeignKey(Product,on_delete=models.CASCADE,default=None)
        pro_name=models.CharField(max_length=100)
        quantity=models.IntegerField()
        price=models.IntegerField()
        total_price=models.IntegerField()

        def __str__(self):
            return self.order


class Order_Rough(models.Model):

        product=models.ForeignKey(Product,on_delete=models.CASCADE,default=None)
        pro_name=models.CharField(max_length=100)
        quantity=models.IntegerField()
        price=models.IntegerField()
        total_price=models.IntegerField()

        def __str__(self):
            return self.pro_name
