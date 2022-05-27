from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.core.paginator import Paginator
from django.shortcuts import render, redirect

from CPL.models import CyclingEvent, User


def show_cycling_events(request):
    # Shows cycling events from DB
    events = CyclingEvent.objects.all().order_by('event_name')
    # Pagination
    p = Paginator(events, per_page=2)
    page = request.GET.get('page')
    events_list = p.get_page(page)

    if 'login_status' in request.COOKIES and 'username' in request.COOKIES:
        return render(request, 'home.html', {
            'events': events_list,
            'username': request.COOKIES['username'],
            'login_status': request.COOKIES['login_status'],
        })

    return render(request, 'home.html', {
        'events': events_list,
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
            response = redirect('home')
            response.set_cookie('username', username)
            response.set_cookie('login_status', True)
            return response
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


def show_user_cookies(request):
    # Shows cookies for logged user when button pressed
    if 'login_status' in request.COOKIES and 'username' in request.COOKIES:
        cookies_context = {
            'username': request.COOKIES['username'],
            'login_status': request.COOKIES['login_status']
        }
        return render(request, 'home.html', cookies_context)

    messages.success(request, 'Login to see your cookies')
    return redirect('home')
