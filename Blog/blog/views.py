from django.shortcuts import render,HttpResponseRedirect
from django.contrib.auth.forms import UserCreationForm
from .forms import SignUpForm,LoginForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from .models import Post
# Create your views here.
def home(request):
    posts= Post.objects.all()
    return render(request,'home.html',{'posts':posts})

def about(request):
    return render(request,'about.html')
    

def about(request):
    return render(request,'about.html')
    
def contact(request):
    return render(request,'contact.html')

def dashboard(request):
    if request.method == "POST":
        posts= Post.object.all()
        return render(request,'dashboard.html',{'posts':posts})
    else:
        return HttpResponseRedirect('/login/')
    

def user_logout(request):
    return HttpResponseRedirect('/')

def user_signup(request):
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            messages.success(request,'congratulations!! you have become an author')
            form.save()
    else:
        form = SignUpForm()
    return render(request,'signup.html',{'form':form})


def user_login(request):
    # if not request.user.is_authenticated:
    if request.method =="POST":
        form=LoginForm(request=request, data=request.POST)
        if form.is_valid():
            uname = form.cleaned_data['username']
            upass = form.cleaned_data['password']
            user = authenticate(username=uname, password=upass)
            if user is not None:
                login(request, user)
                messages.success(request,'Logged in successfully !!')
                return HttpResponseRedirect('/dashboard')
    else:
        form= LoginForm()
    return render(request,'login.html',{'form':form})
    # else:
    #     return HttpResponseRedirect('/dashboard')
# render(request,'login.html',{'form':form}), 

def user_logout(request):
    logout(request)
    return HttpResponseRedirect('/')