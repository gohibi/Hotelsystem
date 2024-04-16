from django import forms
from django.contrib.auth.forms import UserCreationForm
from userauths.models import Profile,User

class UserForm(UserCreationForm):
    full_name = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'enter full name' , 'class':'form-control'}))
    username = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'enter username' , 'class':'form-control'}))
    email = forms.EmailField(widget=forms.TextInput(attrs={'placeholder':'enter email' , 'class':'form-control'}))
    phone = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'enter phone' , 'class':'form-control'}))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder':'enter password' , 'class':'form-control'}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder':'confirm password' , 'class':'form-control'}))
    class Meta:
        model = User
        fields =['full_name','username','email','phone','password1','password2']