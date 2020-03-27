from django.shortcuts import render, redirect
from .forms import UserRegisterForm
from django.contrib import messages
from django.contrib.auth import authenticate
# Create your views here.
from .models import Post, Users


def User(request):
    if request.method == 'POST':
        p = request.POST
        u = Users.objects.all().values()
        li = []
        print(p.get('username'))
        for i in u:
            li.append(i['username'])
        print(li)
        if p.get('username') not in li:
            f = Users()
            f.first_name = p.get('fname')
            f.last_name = p.get('lname')
            f.email = p.get('email')
            f.password = p.get('pwd')
            f.username = p.get('username')
            f.save()
            context = {'post': Users.objects.all()}
            return redirect('/post', context)
        else:
            context = {'post': Users.objects.all(),  p.get('username'): 'u2'}
            return render(request, 'UserApp/Registeration.html', context)
    context = {'post': Users.objects.all()}
    return render(request, 'UserApp/Registeration.html', context)


def login(request):
    if request.method == 'POST':
        p = request.POST
        u = Users.objects.all().values()
        li = []
        # print(p.get('username'))
        for i in u:
            li.append(i['username'])
        # print(li)
        li2 = []
        # print(p.get('password'))
        for i in u:
            li2.append(i['password'])
        # print(li)
        if p.get('username') in li and p.get('pwd') in li2:
            context = {'post': Users.objects.all()}
            return redirect('/post', context)
        else:
            context = {'post': Users.objects.all()}
            return render(request, 'UserApp/Login.html', context)
    context = {'post': Users.objects.all()}
    return render(request, 'UserApp/Login.html', context)


def post(request):
    if request.method == 'POST':
        r = request.POST
        print('asdfqef')
        p = Post()
        p.text = r.get('comment')
        p.save()
        context = {'post': Post.objects.all()}
        return render(request, 'UserApp/Posting.html', context)
    context = {'post': Post.objects.all()}
    return render(request, 'UserApp/Posting.html', context)


