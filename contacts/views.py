from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseServerError
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate


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
                user = User.objects.create_user(username, email, password)
                print(user)
                user.save()
                return redirect('sign-in')
            except :
                return render(request, 'sign_up.html', {
                'error':'Username or Email already exists'
                })
        return render(request, 'sign_up.html', {
            'error':'Password do not match'
            })
        

def sign_in(request):
    if request.method == 'GET':
        return render(request, 'login.html')    
    else:
        try:
            username = request.POST['username']
            password = request.POST['password']

            user = authenticate(request, username=username, password=password)

            if user is None:
                return render(request, 'login.html', {
                "error ": "Invalid credentials"
            })
            else:
                login(request, user)
                return redirect('contacts')
        except:
            return render(request, 'login.html', {
                "error ": "Invalid credentials"
            })




def contacts(request):
    return render(request, 'contacts.html')