from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


# Create your views here.

def main(request):
    return render(request, 'main.html')


def sign_up(request):

    if request.method == 'GET':
        return render(request, 'sign_up.html')
    else: 
        if request.POST['password1'] == request.POST['password2']:
            try:
                username = request.POST['username']
                email = request.POST['email']
                password = request.POST['password1']
                user = User.objects.create_user(username=username, email=email, password=password)
                user.save()
                return redirect('contacts')
            except:
                return render(request, 'sign_up.html', {
                'error':'Username or Email already exists'
                })
        else:
              return render(request, 'sign_up.html', {
                'error':'Password do not match'
                })
        

def sign_in(request):

    if request.method == 'POST':
        print(request.POST)
       # User.check() 
    else:
        print('nothig to do')

    return render(request, 'login.html', {
        "next": "/contacts" # Redirect to dashboard after login,
    })


def contacts(request):
    return render(request, 'contacts.html')