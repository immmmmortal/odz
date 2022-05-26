from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect, reverse


def login_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            response = redirect('/')
            # Setting the cookies
            response.set_cookie('username', username)
            response.set_cookie('login_status', True)
            return response
        else:
            # Return an 'invalid login' error message.
            messages.success(request, 'invalid login')
            return redirect('/member/login_user')

    else:
        return render(request, 'login.html', {})


def logout_user(request):
    logout(request)
    messages.success(request, 'Successfully logged out')
    response = HttpResponseRedirect(reverse('login_user'))
    # Deleting cookies
    response.delete_cookie('username')
    response.delete_cookie('login_status')

    return response


def register_user(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['email']
            password = form.cleaned_data['password1']
            user = authenticate(username, password)
            login(request, user)
            messages.success(request, 'Registration successful')
            return redirect('home')
    else:
        form = UserCreationForm()

    return render(request, 'register.html', {
        'form': form,
    })
