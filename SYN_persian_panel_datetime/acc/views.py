from django.shortcuts import render,redirect
from rest_framework.response import Response
from django.contrib import messages
from django.contrib.auth.models import User,auth
from rest_framework.decorators import api_view , permission_classes
from rest_framework.permissions import IsAuthenticated
def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('/')
        else:
            messages.info(request,'user or pass is not valid')
            return redirect('login')
    else:
        return render(request,'login.html')
def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        if password2 == password1:
            if User.objects.filter(username = username).exists():
                messages.info(request,'user taken')
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.info(request,'email taken')
                return redirect('register')
            else:
                user = User.objects.create_user(username=username,password=password1,email=email,first_name=first_name,last_name=last_name)
                print('user created!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!')
                user.save;
                return redirect('login')
        else:
            messages.info(request,'password not match')
            return redirect('register')
    else:
        return render(request,'register.html')

def logout(request):
    auth.logout(request)
    return redirect('/')

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def example_view(request, format=None):
    content = {
        'user': str(request.user),  # `django.contrib.auth.User` instance.
        'auth': str(request.auth),  # None
        'first_name' : str(request.user.first_name),
        'last_name': str(request.user.last_name),
        'email': str(request.user.email),
        'date_joined': str(request.user.date_joined)
    }
    return Response(content)

