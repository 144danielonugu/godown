from django.shortcuts import render,redirect,get_object_or_404
from address.models import Address
from django.contrib.auth.models import User,auth
# Create your views here.
def logout(request):
    auth.logout(request)
    return redirect("home")
def home(request):
    return render(request,'home.html')
def address(request):
    obj=Address.objects.all()
    return render(request,'address.html',{'text':obj})
def login(request):
    if request.method=="POST":
        username=request.POST["name"]
        passcode=request.POST["pass"]
        user=auth.authenticate(username=username,password=passcode)
        if user is not None:
            auth.login(request,user)
            return redirect("home")
    return render(request,'login.html')
def maddress(request,id):
    obj=get_object_or_404(Address,id=id)
    return render(request,'maddress.html',{"det":obj})