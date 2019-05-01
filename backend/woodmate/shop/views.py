from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from shop.forms import *
from shop.models import *
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required, permission_required

# Create your views here.
def index(request):
    return render(request, template_name='shop/index.html')

def register(request):
    context = {}
    if request.method == 'POST':
        user = UserForm(request.POST)
        form = CustomerForm(request.POST)
        if form.is_valid() and user.is_valid():
            username = request.POST.get('username')
            password = request.POST.get('password')
            email = request.POST.get('email')
            new_user = User.objects.create_user(username, email, password)
            customer = Customer.objects.create(
                first_name=request.POST.get('first_name'),
                last_name=request.POST.get('last_name'),
                email=request.POST.get('email'),
                phone_number=request.POST.get('phone_number'),
                user=new_user
            )
            return redirect('index')
        else:
            print('no')
    else:
        user = UserForm()
        form = CustomerForm()
        
    context['user'] = user
    context['form'] = form
    return render(request, template_name='shop/register.html', context=context)

def my_login(request):
    context = {}

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user:
            login(request, user)

            next_url = request.POST.get('next_url')
            if next_url:
                return redirect(next_url)
            else:
                return  redirect('index')
        else:
            error = 'Wrong username or password!'

            context['username'] = username
            context['password'] = password
            context['error'] = error

    next_url = request.GET.get('next')
    if next_url:
        context['next_url'] = next_url

    return render(request, 'shop/login.html', context=context)

@login_required
def my_logout(request):
    logout(request)
    return redirect('login')

@login_required
def address(request):
    context = {}
    user = request.user
    customer = Customer.objects.get(user=user)
    address = Address.objects.filter(cid = customer)
    context['address'] = address
    return render(request, template_name='shop/address.html', context=context)

@login_required
def add_address(request):
    context = {}
    user = request.user
    customer = Customer.objects.get(user=user)
    if request.method == 'POST':
        form = AddressForm(request.POST)
        if form.is_valid():
            address = Address.objects.create(
                address_desc = request.POST.get('address_desc'),
                district = request.POST.get('district'),
                area = request.POST.get('area'),
                province = request.POST.get('province'),
                postal_code = request.POST.get('postal_code'),
                cid = customer
            )
            return redirect('address')
    else:
        form = AddressForm()
    
    context['form'] = form
    return render(request, template_name='shop/add_address.html', context=context)

@login_required
def del_address(request, address_id):
    address = Address.objects.get(address_id=address_id)
    address.delete()
    return redirect('address')

@login_required
def edit_address(request, address_id):
    context = {}
    address = Address.objects.get(address_id=address_id)
    data = {}
    data['address_desc'] = address.address_desc
    data['district'] = address.district
    data['area'] = address.area
    data['province'] = address.province
    data['postal_code'] = address.postal_code
    if request.method == 'POST':
        form = AddressForm(request.POST)
        if form.is_valid():
            address.address_desc = request.POST.get('address_desc')
            address.district = request.POST.get('district')
            address.area = request.POST.get('area')
            address.province = request.POST.get('province')
            address.postal_code = request.POST.get('postal_code')
            address.save()
            return redirect('address')
    else:
        form = AddressForm(initial=data)
    context['form'] = form
    context['address'] = address
    return render(request, template_name='shop/edit_address.html', context=context)
