from django import forms
from django.core import validators
from django.core.exceptions import ValidationError
from django.contrib.auth import authenticate
from shop.models import *

class CustomerForm(forms.Form):
    first_name = forms.CharField(max_length=50, required=True)
    last_name = forms.CharField(max_length=50, required=True)
    phone_number = forms.CharField(max_length=10, required=True)

    first_name.widget.attrs.update({'class': 'form-control', 'placeholder': 'First Name'})
    last_name.widget.attrs.update({'class': 'form-control', 'placeholder': 'Last Name'})
    phone_number.widget.attrs.update({'class': 'form-control', 'placeholder': 'eg. 089-147-xxxx'})

class AddressForm(forms.Form):
    address_desc = forms.CharField(max_length=500, required=True, widget=forms.Textarea)
    district = forms.CharField(max_length=50, required=True)
    area = forms.CharField(max_length=50, required=True)
    province = forms.CharField(max_length=50, required=True)
    postal_code = forms.CharField(max_length=5, required=True)

def validate_passlen(value):
    if len(value) < 8:
        raise ValidationError('รหัสผ่าน ต้องมีความยาวอย่างน้อย 8 ตัวอักษร')

class UserForm(forms.Form):
    username = forms.CharField(label='ชื่อผู้ใช้', max_length=100, required=True)
    password = forms.CharField(label='รหัสผ่าน', max_length=100, required=True, validators=[validate_passlen], widget=forms.PasswordInput)
    confirmpass = forms.CharField(label='ยืนยันรหัสผ่าน', max_length=100, required=True, widget=forms.PasswordInput)
    email = forms.EmailField(required=True)

    email.widget.attrs.update({'class': "form-control",
                    'aria-describedby': "emailHelp",
                    'placeholder':"eg.woodmate@furniture.com"})
    password.widget.attrs.update({'class': 'form-control', 'placeholder': 'Password'})
    confirmpass.widget.attrs.update({'class': 'form-control', 'placeholder': 'Confirm Password'})
    username.widget.attrs.update({'class': 'form-control', 'placeholder': 'Username'})

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        confirmpass = cleaned_data.get('confirmpass')
        if password != confirmpass:
            raise ValidationError('รหัสผ่าน และ ยืนยันรหัสผ่าน ต้องเหมือนกัน')

class FeedbackModelForm(forms.ModelForm):
    class Meta:
        model = Feedback
        fields = '__all__'

class MakeOrderForm(forms.Form):
    payment = forms.CharField(max_length=50)
    status = forms.CharField(max_length=30, widget=forms.HiddenInput)
    date = forms.DateField(widget=forms.HiddenInput)
