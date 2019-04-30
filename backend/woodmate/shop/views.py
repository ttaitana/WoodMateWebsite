from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from shop.forms import CustomerForm, AddressModelForm, UserForm
from shop.models import Customer, Address

# Create your views here.
def index(request):
    return render(request, template_name='shop/index.html')

def register(request):
    context = {}
    if request.method == 'POST':
        i = 1
        count = 0
        while count < 10:
            count += 1
            try:
                print(i)
                print(Customer.objects.get(cid=i))
            except:
                print('yayaaaa')
                break
            i += 1
        print(i)
        user = UserForm(request.POST)
        form = CustomerForm(request.POST)
        if form.is_valid() and user.is_valid():
            username = request.POST.get('username')
            password = request.POST.get('password')
            email = request.POST.get('email')
            new_user = User.objects.create_user(username, email, password)
            customer = Customer.objects.create(
                cid = i,
                first_name=request.POST.get('first_name'),
                last_name=request.POST.get('last_name'),
                email=request.POST.get('email'),
                phone_number=request.POST.get('phone_number'),
                user=new_user
            )
            print('check')
        else:
            print('no')
    else:
        user = UserForm()
        form = CustomerForm()
        
    context['user'] = user
    context['form'] = form
    return render(request, template_name='shop/register.html', context=context)
