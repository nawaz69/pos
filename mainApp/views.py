from django.shortcuts import render, redirect
from django.contrib.auth.models import User,auth
from django.contrib.auth.decorators import login_required
from .models import Order,Product,Customers,Order_Detail,Order_Rough

# Create your views here.

vat=int(0)
discount=int(0)
gross_total=int(0)
net_amount=int(0)



@login_required(login_url="admin/")
def index(request):
    return render(request,'index.html')

def logout_view(request):
    logout(request)
    return redirect("/")




# kfshdkfskufhsughsig
@login_required(login_url="/")
def take_order(request):
    products=Product.objects.all().order_by('date')
    ord=Order_Rough.objects.all()
    vat=int(0)
    discount=int(0)
    gross_total=int(0)
    net_amount=int(0)
    if request.method == "POST":
        # Filter restaurants by selected region, but only on a POST
        pro_name = request.POST["products"]
        qty=request.POST["qty"]
       
        product = products.get(id=pro_name)
        
        
        

        print("\n\n ==>Product Name     \n\n\n")
        print(pro_name)
        print("\n\n ==>Quantity     \n\n\n")
        print(qty)
        print("\n\n ==>Product     \n\n\n")
        print(product.name)
        print("\n\n ==>Product     \n\n\n")
        print("^^^^^")

        
        

        b = Order_Rough(pro_name=product.name, quantity=qty,total_price=(int(qty)*int(product.price)),product_id=product.id,price=product.price)
        b.save()
        gross_total=int(0)
        for p in ord:
            gross_total=gross_total+int(p.total_price)
        vat=(gross_total*17)/100
        vat=vat+gross_total
        net_amount=vat-discount


        ord=Order_Rough.objects.all()
       

    
    return render(request,'takeorders.html',{'product':products,'ord':ord,'gt':gross_total,'vat':vat,'net_amount':net_amount})



# kfshdkfskufhsughsig
@login_required(login_url="/")
def reports(request):
    return render(request,'reports.html')

@login_required(login_url="/")
def tables(request):
    return render(request,'tables.html')

    

def logout(request):
    auth.logout(request)
    return ('/')


def clearRoughOrder(request):
    
    Order_Rough.objects.all().delete()
    products=Product.objects.all().order_by('date')
    ord=Order_Rough.objects.all()
    print("\n\n\n olalala\n\n\n\nn\n")
    ord=Order_Rough.objects.all()
    print("\n\n\n olalala\n\n\n\nn\n")
    return redirect("/orders")


def makeOrder(request):

    order = Order(paid=0,table=1, customer_id=1 ,actual_price=gross_total,discounted_price=0,grand_total=net_amount,taken_by_id=request.user.id)
    order.save()
    ord_rough=Order_Rough.objects.all()
    for o in ord_rough:       
       ord_detail=Order_Detail(order_id=order.id,product_id=o.product_id,pro_name=o.pro_name,quantity=o.quantity,price=o.price,total_price=o.total_price)
       ord_detail.save()
    

    return redirect("/clearRough")
 
 

