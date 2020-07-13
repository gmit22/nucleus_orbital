from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect

from accounts.models import BookingManager


def index(request):
	return render(request, 'accounts/login.html')

def register(request):

    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():

            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            bm = BookingManager(userid=username, upcoming_bookings="", past_bookings="")
            bm.save()
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return render(request, 'accounts/register.html', {'form': form, 'absoluteurl': '/auth/login/'})
    else:
        form = UserCreationForm()
    return render(request, 'accounts/register.html', {'form': form, 'absoluteurl': '/auth/login/'})

