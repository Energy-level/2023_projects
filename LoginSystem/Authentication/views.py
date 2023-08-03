from django.http import HttpResponse
from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib import messages 
from django.contrib.auth import authenticate,login,logout
from django.core.mail import send_mail
from webapp import settings

# Create your views here.
def home(request):
    return render(request,"Authentication/index.html")
def signup(request):
    if request.method=="POST":
        username=request.POST['uid']
        fname=request.POST['fname']
        lname=request.POST['lname']
        email=request.POST['email1']
        pass1=request.POST['pass1']
        if User.objects.filter(username=username):
            messages.error(request,"user name is already existed")
            return redirect("home")
        if User.objects.filter(email=email):
            messages.error(request,"email is already existed")
            return redirect("home")
        if not username.isalnum():
            messages.error(request,"user name must be alpha numeric")
        myuser=User.objects.create_user(username, email, pass1)
        myuser.first_name=fname
        myuser.last_name=lname
        myuser.save()
        messages.success(request,"your account has been created successfully. we seng you an confirmation eamil, please confirm your email inorder to activate your account")

        # for email mag

        subject="welcome to fitness assistent........."
        message="hello "+ myuser.first_name +" welcome to our website \n thank you for visiting our website"
        from_email=settings.EMAIL_HOST_USER
        to_list=[myuser.email]
        send_mail(subject,message,from_email,to_list,fail_silently=True)

        return redirect('signin_link')
    return render(request,"Authentication/signup.html")
def signin(request):
    if request.method=="POST":
        use=request.POST['use']
        pas=request.POST['pas']
        user=authenticate(username=use,password=pas)
        if user is not None:
            login(request,user)
            fname=user.first_name
            return render(request,"Authentication/index.html",{"fname":fname})
        else:
            messages.error(request,"please add credintials")
            return redirect('home')
    return render(request,"Authentication/signin.html")
def signout(request):
    logout(request)
    messages.success(request,"your'we logout successfully!!!!")
    return redirect('home')
