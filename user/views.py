from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from .models import User
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import login, authenticate, logout
# Create your views here.
def signup_view(request):
    if request.method == 'GET':
        return render(request, 'user/signup.html')
    elif request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        email = request.POST['email']
        if not username:
            return HttpResponse("用户名不能为空")
        if User.objects.filter(username=username):
            return HttpResponse("用户名已存在")
        user = User.objects.create_user(username=username, password=password, email=email)
        user.save()
        login(request, user)
        return HttpResponseRedirect("/index")

def login_view(request):
    if request.method == 'GET':
        print(not request.user.is_authenticated)
        if request.user.is_authenticated:
            login(request, request.user)
            return HttpResponseRedirect('/index')
        return render(request, 'user/login.html')
    elif request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if not user:
            return HttpResponse("用户名或密码不正确")
        else:
            login(request, user)
        return HttpResponseRedirect("/index")
    pass

@login_required()
def updatepwd(request):
    if request.method == 'GET':
        data = {
            'username': request.user
        }
        return render(request, "user/updatepwd.html", data)
    elif request.method == 'POST':
        username = request.POST.get("username")
        password = request.POST.get("password1")
        password_new = request.POST.get("password2")
        user = authenticate(username=username, password=password)
        if not user:
            return HttpResponse("用户不存在")
        try:
            user.set_password(password_new)
            user.save()
        except:
            return HttpResponse("修改密码失败！")
    return HttpResponse("修改成功")

@login_required()
def info(request):
    if request.method == 'GET':
        username = request.user
        user = User.objects.get(username=username)
        data = {
            'username': user.username,
            'firstname': user.first_name,
            'lastname': user.last_name,
            'email': user.email,
            'created_time': user.date_joined
        }
        return render(request, "user/userinfo.html", data)
    elif request.method == 'POST':
        user = User.objects.get(username=request.user)
        user.first_name = request.POST.get('firstname')
        user.last_name = request.POST.get('lastname')
        user.email = request.POST.get('email')
        user.joined_time = request.POST.get('created_time')
        user.save()
        return HttpResponse("修改成功")

@login_required()
def logout_view(request):
    logout(request)
    return HttpResponseRedirect("/user/login/")