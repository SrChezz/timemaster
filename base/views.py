from django.shortcuts import redirect, render
from django.http import HttpResponse  
from .models import Alarm
from .forms import AlarmForm
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

def say_hello(request):
  return render(request, 'hello.html')

def view_alarms(request):
  alarms = Alarm.objects.all()
  context = {'alarms': alarms}
  return render(request, 'alarms.html', context) 


@login_required(login_url='/login')
def create_alarm(request):
  form = AlarmForm()

  if request.method == 'POST':
      form = AlarmForm(request.POST)
      if form.is_valid():
         form.save()
         return redirect('home')

  context = {'form': form}
  return render(request, 'form.html', context)

def loginPage(request):
   
   if request.method == 'POST':
    username = request.POST.get('username')
    password = request.POST.get('password')

    try:
      user = User.objects.get(username=username);
    except:
      messages.error(request, 'El usuario no existe')

    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        return redirect('home')
    else:
       messages.error(request,  'User or passwrod does not exist')

   context = {}
   return render(request, 'login.html', context)

def logoutUser(request):
   logout(request)
   return redirect('login')