from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User, Group
from shop.forms import *
from shop.models import *
import datetime
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required, permission_required

# Create your views here.
province = [
    {
        "pid": "10",
        "name": "กรุงเทพมหานคร"
    },
    {
        "pid": "11",
        "name": "สมุทรปราการ"
    },
    {
        "pid": "12",
        "name": "นนทบุรี"
    },
    {
        "pid": "13",
        "name": "ปทุมธานี"
    },
    {
        "pid": "14",
        "name": "พระนครศรีอยุธยา"
    },
    {
        "pid": "15",
        "name": "อ่างทอง"
    },
    {
        "pid": "16",
        "name": "ลพบุรี"
    },
    {
        "pid": "17",
        "name": "สิงห์บุรี"
    },
    {
        "pid": "18",
        "name": "ชัยนาท"
    },
    {
        "pid": "19",
        "name": "สระบุรี"
    },
    {
        "pid": "20",
        "name": "ชลบุรี"
    },
    {
        "pid": "21",
        "name": "ระยอง"
    },
    {
        "pid": "22",
        "name": "จันทบุรี"
    },
    {
        "pid": "23",
        "name": "ตราด"
    },
    {
        "pid": "24",
        "name": "ฉะเชิงเทรา"
    },
    {
        "pid": "25",
        "name": "ปราจีนบุรี"
    },
    {
        "pid": "26",
        "name": "นครนายก"
    },
    {
        "pid": "27",
        "name": "สระแก้ว"
    },
    {
        "pid": "30",
        "name": "นครราชสีมา"
    },
    {
        "pid": "31",
        "name": "บุรีรัมย์"
    },
    {
        "pid": "32",
        "name": "สุรินทร์"
    },
    {
        "pid": "33",
        "name": "ศรีสะเกษ"
    },
    {
        "pid": "34",
        "name": "อุบลราชธานี"
    },
    {
        "pid": "35",
        "name": "ยโสธร"
    },
    {
        "pid": "36",
        "name": "ชัยภูมิ"
    },
    {
        "pid": "37",
        "name": "อำนาจเจริญ"
    },
    {
        "pid": "38",
        "name": "บึงกาฬ"
    },
    {
        "pid": "39",
        "name": "หนองบัวลำภู"
    },
    {
        "pid": "40",
        "name": "ขอนแก่น"
    },
    {
        "pid": "41",
        "name": "อุดรธานี"
    },
    {
        "pid": "42",
        "name": "เลย"
    },
    {
        "pid": "43",
        "name": "หนองคาย"
    },
    {
        "pid": "44",
        "name": "มหาสารคาม"
    },
    {
        "pid": "45",
        "name": "ร้อยเอ็ด"
    },
    {
        "pid": "46",
        "name": "กาฬสินธุ์"
    },
    {
        "pid": "47",
        "name": "สกลนคร"
    },
    {
        "pid": "48",
        "name": "นครพนม"
    },
    {
        "pid": "49",
        "name": "มุกดาหาร"
    },
    {
        "pid": "50",
        "name": "เชียงใหม่"
    },
    {
        "pid": "51",
        "name": "ลำพูน"
    },
    {
        "pid": "52",
        "name": "ลำปาง"
    },
    {
        "pid": "53",
        "name": "อุตรดิตถ์"
    },
    {
        "pid": "54",
        "name": "แพร่"
    },
    {
        "pid": "55",
        "name": "น่าน"
    },
    {
        "pid": "56",
        "name": "พะเยา"
    },
    {
        "pid": "57",
        "name": "เชียงราย"
    },
    {
        "pid": "58",
        "name": "แม่ฮ่องสอน"
    },
    {
        "pid": "60",
        "name": "นครสวรรค์"
    },
    {
        "pid": "61",
        "name": "อุทัยธานี"
    },
    {
        "pid": "62",
        "name": "กำแพงเพชร"
    },
    {
        "pid": "63",
        "name": "ตาก"
    },
    {
        "pid": "64",
        "name": "สุโขทัย"
    },
    {
        "pid": "65",
        "name": "พิษณุโลก"
    },
    {
        "pid": "66",
        "name": "พิจิตร"
    },
    {
        "pid": "67",
        "name": "เพชรบูรณ์"
    },
    {
        "pid": "70",
        "name": "ราชบุรี"
    },
    {
        "pid": "71",
        "name": "กาญจนบุรี"
    },
    {
        "pid": "72",
        "name": "สุพรรณบุรี"
    },
    {
        "pid": "73",
        "name": "นครปฐม"
    },
    {
        "pid": "74",
        "name": "สมุทรสาคร"
    },
    {
        "pid": "75",
        "name": "สมุทรสงคราม"
    },
    {
        "pid": "76",
        "name": "เพชรบุรี"
    },
    {
        "pid": "77",
        "name": "ประจวบคีรีขันธ์"
    },
    {
        "pid": "80",
        "name": "นครศรีธรรมราช"
    },
    {
        "pid": "81",
        "name": "กระบี่"
    },
    {
        "pid": "82",
        "name": "พังงา"
    },
    {
        "pid": "83",
        "name": "ภูเก็ต"
    },
    {
        "pid": "84",
        "name": "สุราษฎร์ธานี"
    },
    {
        "pid": "85",
        "name": "ระนอง"
    },
    {
        "pid": "86",
        "name": "ชุมพร"
    },
    {
        "pid": "90",
        "name": "สงขลา"
    },
    {
        "pid": "91",
        "name": "สตูล"
    },
    {
        "pid": "92",
        "name": "ตรัง"
    },
    {
        "pid": "93",
        "name": "พัทลุง"
    },
    {
        "pid": "94",
        "name": "ปัตตานี"
    },
    {
        "pid": "95",
        "name": "ยะลา"
    },
    {
        "pid": "96",
        "name": "นราธิวาส"
    }
]

def index(request):
    context = {}
    check = 0
    try:
      customer = Customer.objects.get(user = request.user)
    except:
      check = 1
    if check == 0 :
      customer = Customer.objects.get(user = request.user)
      cart = Cart.objects.filter(cid = customer)
      num = 0
      for c in cart:
        num += c.unit
      context['numofproduct'] = num
    return render(request, template_name='shop/index.html', context=context)


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
            my_group = Group.objects.get(name='Customer')
            my_group.user_set.add(new_user)
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
            groups = request.user.groups.filter(name="Sales")
            for g in groups:
                if g.name == 'Sales':
                    return redirect('/admin')
            groups = request.user.groups.filter(name="Delivery Man")
            for g in groups:
                if g.name == 'Delivery Man':
                    return redirect('/admin')

            next_url = request.POST.get('next_url')
            if next_url:
                return redirect(next_url)
            else:
                return redirect('index')
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
    check = 0
    try:
      customer = Customer.objects.get(user = request.user)
    except:
      check = 1
    if check == 0 :
      customer = Customer.objects.get(user = request.user)
      cart = Cart.objects.filter(cid = customer)
      num = 0
      for c in cart:
        num += c.unit
      context['numofproduct'] = num
    context['provinces'] = province
    user = request.user
    customer = Customer.objects.get(user=user)
    if request.method == 'POST':
        form = AddressForm(request.POST)
        if form.is_valid():
            try:
                address = Address.objects.get(cid=customer)
                address.address_desc = request.POST.get('address_desc')
                address.district = request.POST.get('district')
                address.area = request.POST.get('area')
                address.province = request.POST.get('province')
                address.postal_code = request.POST.get('postal_code')
                address.save()
                return redirect('address')
            except:
                address = Address.objects.create(
                    address_desc=request.POST.get('address_desc'),
                    district=request.POST.get('district'),
                    area=request.POST.get('area'),
                    province=request.POST.get('province'),
                    postal_code=request.POST.get('postal_code'),
                    cid=customer
                )
                address.save()
                return redirect('address')
    try:
        address = Address.objects.get(cid=customer)
        context['address'] = address
        data = {}
        data['address_desc'] = address.address_desc
        data['district'] = address.district
        data['area'] = address.area
        data['province'] = address.province
        data['postal_code'] = address.postal_code
        form = AddressForm(initial=data)
        context['form'] = form
        return render(request, template_name='shop/address.html', context=context)
    except:
        pass
    form = AddressForm()
    context['form'] = form
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
                address_desc=request.POST.get('address_desc'),
                district=request.POST.get('district'),
                area=request.POST.get('area'),
                province=request.POST.get('province'),
                postal_code=request.POST.get('postal_code'),
                cid=customer
            )
            return redirect('address')
    else:
        return redirect('address')


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


@login_required
def feedback(request):
    context = {}
    check = 0
    try:
      customer = Customer.objects.get(user = request.user)
    except:
      check = 1
    if check == 0 :
      customer = Customer.objects.get(user = request.user)
      cart = Cart.objects.filter(cid = customer)
      num = 0
      for c in cart:
        num += c.unit
      context['numofproduct'] = num
    if request.method == 'POST':
        form = FeedbackForm(request.POST)
        feedback = Feedback.objects.create(
            text=request.POST.get('text')
        )
        feedback.save()
    else:
        pass
    form = FeedbackForm()
    context['form'] = form
    return render(request, template_name='shop/feedback.html', context=context)


def viewAllItem(request, type_id):
    context = {}
    check = 0
    try:
      customer = Customer.objects.get(user = request.user)
    except:
      check = 1
    if check == 0 :
      customer = Customer.objects.get(user = request.user)
      cart = Cart.objects.filter(cid = customer)
      num = 0
      for c in cart:
        num += c.unit
      context['numofproduct'] = num
    types = ProductType.objects.all()
    if type_id != 0:
        gettype = ProductType.objects.get(ptype_id=type_id)
        items = Product.objects.filter(product_type=gettype)
    else:
        items = Product.objects.all()
    context['item'] = items
    context['types'] = types
    return render(request, template_name='shop/view_items.html', context=context)


def itemDetails(request, product_id):
    context = {}
    product = Product.objects.get(product_id=product_id)
    context['item'] = product
    return render(request, template_name='shop/itemDetails.html', context=context)


@login_required
def addToCart(request, product_id):
    number = request.POST.get('number')
    number = int(number)
    if number <= 0:
        return redirect('viewitems', type_id=0)
    product = Product.objects.get(product_id=product_id)
    customer = Customer.objects.get(user=request.user)
    try:
        print(Cart.objects.get(pid=product, cid=customer))
        cart = Cart.objects.get(pid=product, cid=customer)
        unit = cart.unit
        unit += number
        cart.unit = unit
        cart.save()
    except:
        cart = Cart.objects.create(
            cid=customer,
            pid=product,
            unit=number
        )
    return redirect('viewitems', type_id=0)


def editCart(request):
    context = {}
    check = 0
    try:
      customer = Customer.objects.get(user = request.user)
    except:
      check = 1
    if check == 0 :
      customer = Customer.objects.get(user = request.user)
      cart = Cart.objects.filter(cid = customer)
      num = 0
      for c in cart:
        num += c.unit
      context['numofproduct'] = num
    customer = Customer.objects.get(user=request.user)
    cart = Cart.objects.filter(cid=customer)
    try:
        address = Address.objects.get(cid=customer)
    except:
        return redirect('add_address')
    address = Address.objects.get(cid=customer)
    totalprice = 0
    totalunit = 0
    for c in cart:
        product = c.pid
        price = product.price * c.unit
        totalprice += price
        c.price = price
        c.image = product.product_pic
        totalunit += c.unit
    today = datetime.datetime.now().date()
    form = MakeOrderForm(initial={'date': today, 'status': 'Waiting'})
    context['cart'] = cart
    context['address'] = address
    context['totalprice'] = totalprice
    context['totalunit'] = totalunit

    if len(cart) > 0:
        context['pricewithdeli'] = totalprice + 250
    else:
        context['pricewithdeli'] = totalprice
    context['form'] = form
    return render(request, template_name='shop/edit_cart.html', context=context)


def plusUnit(request, cart_id):
    cart = Cart.objects.get(cart_id=cart_id)
    unit = cart.unit
    unit += 1
    cart.unit = unit
    cart.save()
    return redirect('editcart')


def minusUnit(request, cart_id):
    cart = Cart.objects.get(cart_id=cart_id)
    unit = cart.unit
    unit -= 1
    cart.unit = unit
    if unit == 0:
        cart.delete()
    else:
        cart.save()
    return redirect('editcart')


def deleteCart(request, cart_id):
    cart = Cart.objects.get(cart_id=cart_id)
    cart.delete()
    return redirect('editcart')


def makeOrder(request):
    context = {}
    customer = Customer.objects.get(user=request.user)
    cart = Cart.objects.filter(cid=customer)
    try:
        address = Address.objects.get(cid=customer)
    except:
        return redirect('add_address')
    if request.method == 'POST':
        form = MakeOrderForm(request.POST)
        if form.is_valid():
            if len(cart) <= 0:
              return redirect('editcart')
            payment = request.POST.get('payment')
            date = request.POST.get('date')
            status = request.POST.get('status')
            order = Order.objects.create(
                payment=payment,
                status=status,
                date=date,
                customer=customer
            )
            totalprice = 0
            for c in cart:
                product = c.pid
                checkunit = product.stock - c.unit
                if checkunit < 0:
                    return redirect('editcart')
                product.stock = checkunit
                price = product.price * c.unit
                totalprice += price
                orderlist = OrderList.objects.create(
                    product=product,
                    unit=c.unit,
                    price=product.price,
                    total_price=price,
                    order=order
                )
                product.save()
                c.delete()
            totalprice += 250
            order.total_price = totalprice
            order.save()

            return redirect('checkorder')
    totalprice = 0
    for c in cart:
        product = c.pid
        price = product.price * c.unit
        totalprice += price
        c.price = price
    today = datetime.datetime.now().date()
    form = MakeOrderForm(initial={'date': today, 'status': 'Waiting'})
    context['form'] = form
    context['cart'] = cart
    context['totalprice'] = totalprice
    return render(request, template_name='shop/make_order.html', context=context)


@login_required
def checkOrder(request):
    context = {}
    customer = Customer.objects.get(user=request.user)
    order = Order.objects.filter(customer=customer)
    context['order'] = order
    return render(request, template_name='shop/check_order.html', context=context)


@login_required
def orderDetails(request, order_id):
    context = {}
    order = Order.objects.get(oid=order_id)
    orderlist = OrderList.objects.filter(order=order)
    context['orderlist'] = orderlist
    context['order'] = order
    return render(request, template_name='shop/order_details.html', context=context)


@login_required
def myProfile(request):
    context = {}
    check = 0
    try:
      customer = Customer.objects.get(user = request.user)
    except:
      check = 1
    if check == 0 :
      customer = Customer.objects.get(user = request.user)
      cart = Cart.objects.filter(cid = customer)
      num = 0
      for c in cart:
        num += c.unit
      context['numofproduct'] = num
    customer = Customer.objects.get(user=request.user)
    if request.method == 'POST':
        customer.first_name = request.POST.get('first_name')
        customer.last_name = request.POST.get('last_name')
        customer.phone_number = request.POST.get('phone_number')
        customer.save()
    data = {}
    data['first_name'] = customer.first_name
    data['last_name'] = customer.last_name
    data['phone_number'] = customer.phone_number
    form = CustomerForm(initial=data)
    context['form'] = form
    context['customer'] = customer
    return render(request, template_name='shop/profile.html', context=context)
