from django.contrib import messages
from django.shortcuts import render

# Create your views here.
from CPL.models import CyclingEvent, EventParticipatingGroup, User


def event_page(request):
    event = CyclingEvent.objects.all()
    group = EventParticipatingGroup

    return render(request, 'home.html', {'events': event})


def register_for_a_ride(request):
    event = CyclingEvent.objects.all()
    if request.method == 'POST':
        full_name = request.POST['full_name_register_for_a_ride']
        email = request.POST['email_register_for_a_ride']
        user = User.objects.create(full_name, email)
        user.save()
        messages.success(request, 'You registered in a ride!')

    return render(request, 'home.html', {'events': event})
