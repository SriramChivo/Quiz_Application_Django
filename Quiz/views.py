from django.shortcuts import render
from django.views import View
from django.contrib.auth import authenticate,login
from django.urls import reverse
from django.http import HttpResponseRedirect


# Create your views here.

class login_auth_implementation(View):

    def post(self,request):
        username_data=request.POST.get("username")
        password_data=request.POST.get("password")
        is_autheticated=authenticate(request,username=username_data,password=password_data)
        if is_autheticated:
            login(request, is_autheticated)
            return HttpResponseRedirect(reverse("quiz-home"))
        else:
            return render(request,"Quiz/home.html",context={"error":"The username and Password not an exact match"})
    def get(self,request):
        return render(request,"Quiz/home.html")
