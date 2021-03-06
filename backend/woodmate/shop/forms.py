from django import forms
from django.core import validators
from django.core.exceptions import ValidationError
from django.contrib.auth import authenticate
from shop.models import *


class CustomerForm(forms.Form):
    first_name = forms.CharField(max_length=50, required=True)
    last_name = forms.CharField(max_length=50, required=True)
    phone_number = forms.CharField(max_length=10, required=True)

    first_name.widget.attrs.update(
        {'class': 'form-control', 'placeholder': 'First Name'})
    last_name.widget.attrs.update(
        {'class': 'form-control', 'placeholder': 'Last Name'})
    phone_number.widget.attrs.update(
        {'class': 'form-control', 'placeholder': 'eg. 089147xxxx'})

    def clean(self):
        cleaned_data = super().clean()
        phone_number = cleaned_data.get('phone_number')
        if phone_number.isdigit():
            pass
        else:
            raise ValidationError('เบอร์โทรศัพท์ต้องเป็นตัวเลขเท่านั้น')


class AddressForm(forms.Form):
    # address_desc = forms.CharField(max_length=500, required=True, widget=forms.Textarea(attrs={'class': 'md-textarea form-control'}))
    address_desc = forms.CharField(max_length=500, required=True)
    district = forms.CharField(max_length=50, required=True)
    area = forms.CharField(max_length=50, required=True)
    province = forms.CharField(max_length=50, required=True)
    postal_code = forms.CharField(max_length=5, required=True)

    address_desc.widget.attrs.update({'class': 'form-control'})
    district.widget.attrs.update({'class': 'form-control'})
    area.widget.attrs.update({'class': 'form-control'})
    province.widget.attrs.update({'class': 'form-control'})
    postal_code.widget.attrs.update({'class': 'form-control'})


def validate_passlen(value):
    if len(value) < 8:
        raise ValidationError('รหัสผ่าน ต้องมีความยาวอย่างน้อย 8 ตัวอักษร')


class UserForm(forms.Form):
    username = forms.CharField(
        label='ชื่อผู้ใช้', max_length=100, required=True)
    password = forms.CharField(label='รหัสผ่าน', max_length=100, required=True, validators=[
                               validate_passlen], widget=forms.PasswordInput)
    confirmpass = forms.CharField(
        label='ยืนยันรหัสผ่าน', max_length=100, required=True, widget=forms.PasswordInput)
    email = forms.EmailField(required=True)

    email.widget.attrs.update({'class': "form-control",
                               'aria-describedby': "emailHelp",
                               'placeholder': "eg.woodmate@furniture.com"})
    password.widget.attrs.update(
        {'class': 'form-control', 'placeholder': 'Password'})
    confirmpass.widget.attrs.update(
        {'class': 'form-control', 'placeholder': 'Confirm Password'})
    username.widget.attrs.update(
        {'class': 'form-control', 'placeholder': 'Username'})

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        confirmpass = cleaned_data.get('confirmpass')
        if len(str(password)) < 8:
            raise ValidationError('รหัสผ่านต้องมีอย่างน้อย 8 ตัวอักษร')
        if password != confirmpass:
            raise ValidationError('รหัสผ่าน และ ยืนยันรหัสผ่าน ต้องเหมือนกัน')


class FeedbackForm(forms.Form):
    text = forms.CharField(max_length=500, widget=forms.Textarea)

    text.widget.attrs.update({
        'class': 'form-control'
    })


class MakeOrderForm(forms.Form):
    cash = 'เงินสด'
    credit = 'CreditCard'
    debit = 'DebitCard'
    payment_choice = {
        (cash, 'เงินสด'),
        (credit, 'Credit Card'),
        (debit, 'Debit Card')
    }
    payment = forms.ChoiceField(widget=forms.RadioSelect, required=True, choices=payment_choice)
    status = forms.CharField(max_length=30, widget=forms.HiddenInput)
    date = forms.DateField(widget=forms.HiddenInput)

    payment.widget.attrs.update(
        {
            
        }
    )

    def clean(self):
        cleaned_data = super().clean()
        payment = cleaned_data.get('payment')
        if len(payment) <= 0:
            raise ValidationError('กรุณาระบุวิธีการจ่ายเงิน')
