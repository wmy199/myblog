from django.shortcuts import render, redirect, reverse
from django.http import HttpResponse
from blog.models import Blog, BlogType
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User


def is_it_has_space_or_is_it_none(string):
    if string == '':
        return True
    for each in string:
        if each == ' ':
            return True
    return False


def home(request):
    context = {}
    blog_types = BlogType.objects.all()
    print(blog_types)
    print('debug')
    context['blog_types'] = blog_types
    return render(request, 'home.html', context)


def mylogin(request):
    username = request.POST.get('username')
    password = request.POST.get('password')
    rd = request.META.get('HTTP_REFERER', '/')
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        return redirect(rd)
    else:
        return HttpResponse('密码错误')


def mylogout(request):
    logout(request)
    rd = request.META.get('HTTP_REFERER', '/')
    return redirect(rd)


def create_account_page(request):
    referer =  request.META.get('HTTP_REFERER','/')
    context = {'referer':referer}
    return render(request, 'create_account_page.html', context)


def create_account(request):
    if request.method == 'POST':
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        passwordagain = request.POST.get('passwordagain')
        email = request.POST.get('email')
        referer = request.POST.get('referer','/')
        if is_it_has_space_or_is_it_none(username) or \
           is_it_has_space_or_is_it_none(password) or \
           is_it_has_space_or_is_it_none(passwordagain) or \
           is_it_has_space_or_is_it_none(email):
            return HttpResponse('用户输入不合法，用户名，密码，邮箱不能为空或含有空格')
        if password != passwordagain:
            return HttpResponse('两次密码不一致')
        try:
            user = User.objects.get(username = username)
        except User.DoesNotExist as identifier:
            user = None
        print(user)
        if user:
            return HttpResponse('用户已存在')
        else:
            user = User.objects.create_user(username,email,password)
            login(request,user)
            return redirect(referer)
        
