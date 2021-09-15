from django.shortcuts import render,redirect
from django.http import HttpResponceRedirect
# Create your views here.
def home_view(request):
    if request.user.is_authenticated:
        return HttpResponceRedirect('after_login')
    return render('hospital.html')
