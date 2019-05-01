from django.urls import path
from . import views

urlpatterns = [
    path('index/', views.index, name='index'),
    path('register/', views.register, name='register'),
    path('login/', views.my_login, name='login'),
    path('logout/', views.my_logout, name='logout'),
    path('address/', views.address, name='address'),
    path('add_address/', views.add_address, name='add_address'),
    path('del_address/<int:address_id>', views.del_address, name='del_address'),
    path('edit_address/<int:address_id>', views.edit_address, name='edit_address'),
    path('feedback/', views.feedback, name='feedback'),
    path('viewitems/', views.viewAllItem, name='viewitems'),
    path('itemdetails/<int:product_id>', views.itemDetails, name='itemdetails'),

]