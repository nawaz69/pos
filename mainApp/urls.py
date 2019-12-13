from django.urls import path
from . import views

app_name="mainApp"
urlpatterns=[
    
path('',views.index,name="index"),  
path('reports/',views.reports,name="reports"),   
path('orders/',views.take_order,name="takeorder"), 
path('logout',views.logout_view,name='logout'),
path('clearRough/',views.clearRoughOrder,name="clearRoughOrder"), 
path('makeOrder/',views.makeOrder,name="makeOrder"),


]