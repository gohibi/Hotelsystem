from django.shortcuts import render , redirect
from userauths.models import Profile,User
from userauths.forms import UserForm
from django.contrib import messages
from django.contrib.auth import login,logout,authenticate
# Create your views here.

def registerView(request):
    # if request.user.is_authenticated:
    #     messages.warning(request,f"you're already logged in ")
    form = UserForm(request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            form.save()
            full_name =form.cleaned_data.get('full_name')
            phone =form.cleaned_data.get('phone')
            email =form.cleaned_data.get('email')
            password =form.cleaned_data.get('password1')
            
            user = authenticate(email=email, password=password)
            login(request , user)
            messages.success(request,f'{full_name}, account has been created successfully !!')

            profile =Profile.objects.get(user = request.user)
            profile.full_name = full_name
            profile.phone = phone
            profile.save()

            return redirect('hotel:index')
    else:
        form = UserForm()
        
    context={
        'form':form
        }
    return render(request,'userauths/register.html',context)

def loginView(request):
  
    return render(request,'userauths/login.html')

def logoutView(request):
  
    return render(request,'userauths/logout.html')