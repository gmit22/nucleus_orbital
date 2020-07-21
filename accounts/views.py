from django.contrib.auth import login, authenticate, update_session_auth_hash
#from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from .forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth.forms import PasswordChangeForm
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
            return render(request, 'accounts/successfulregistration.html', {'username':username})
    else:
        form = UserCreationForm()
    return render(request, 'accounts/register.html', {'form': form, 'absoluteurl': '/auth/login/'})


def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Important!
            messages.success(request, 'Your password was successfully updated!')
            return redirect('http://127.0.0.1:8000/')
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'accounts/change_password.html', {
        'form': form
    })
