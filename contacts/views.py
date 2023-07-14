from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


# Create your views here.

def main(request):
    return render(request, 'contacts.html')


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
                return HttpResponse('User created!')
            except:
                return render(request, 'sign_up.html', {
                'form': UserCreationForm,
                'message':'Username or Email already exists'
                })
        else:
              return render(request, 'sign_up.html', {
                  'form': UserCreationForm,
                'message':'Password do not match'
                })


def contacts(request):
    return HttpResponse('CONTACTOS')