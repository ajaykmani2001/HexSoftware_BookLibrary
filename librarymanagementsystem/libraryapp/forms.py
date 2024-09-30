from django import forms
from django.forms import ModelForm
from django.contrib.auth.models import User
from .models import *



class student(forms.ModelForm):
    my_choice=(
        ('CSE','CSE'),
        ('EEE','EEE'),
        ('MECH', 'MECH'),
        ('CIVIL', 'CIVIL'),
        ('EC', 'EC'),
    )
    dept = forms.ChoiceField(label='Department', choices=my_choice)
    college_name=forms.CharField(label='College ')
    password = forms.CharField(label='password', widget=forms.PasswordInput)
    cpassword = forms.CharField(label='confirm password', widget=forms.PasswordInput)
    roll_no = forms.IntegerField(label='Roll Number')
    reg_no = forms.CharField(label='Register Number')
    phone=forms.IntegerField()
    class Meta:
        model = User
        fields = ['username','first_name','last_name', 'email', 'password','cpassword', 'college_name' ,'reg_no', 'roll_no','phone','dept']
#
#






class bookform(forms.ModelForm):
    book_image=forms.ImageField(label='Book Image')
    book_name=forms.CharField()
    author=forms.CharField()
    book_id=forms.CharField()
    description=forms.CharField()
    # ISBN=forms.CharField()
    available_copies=forms.IntegerField()
    genre=forms.CharField()

    class Meta:
        model=BookModel
        fields=['book_image','book_name','author','genre','book_id','description','available_copies']





