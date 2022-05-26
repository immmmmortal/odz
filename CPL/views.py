from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect

from CPL.models import CyclingEvent, User


def show_cycling_events(request):
    events = CyclingEvent.objects.all()
    return render(request, 'home.html', {
        'events': events
    })


def login_user_from_modal(request):
    # Login user from popup modal
    if request.method == 'POST':
        username = request.POST['username_login_through_modal']
        password = request.POST['password_login_through_modal']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, 'Successful login')
            return redirect('home')
        else:
            # Return an 'invalid login' error message.
            messages.success(request, 'Invalid login')
            return redirect('login_user')


def register_user_for_a_ride(request):
    # Register in a ride logged users,propose to log in for not logged users,propose to registrate for new users
    if request.method == 'POST':
        full_name = request.POST['full_name_of_logged_user']
        email = request.POST['email_of_logged_user']
        user = User.objects.create(full_name=full_name, email=email)
        user.save()
        messages.success(request, 'Successful registration')
        return redirect('home')

    return render(request, 'home.html')
