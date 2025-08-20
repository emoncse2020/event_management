from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Event, Participant, Category
from .forms import EventForm
from django.db.models import Count, Q
from django.utils import timezone
def create_event(request):
    form = EventForm()
    if request.method == "POST":
        form = EventForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Event created successfully")

    context = {
        "form" : form
    }

    return render(request, 'events/event_form.html', context)

def get_dashboard_stats():
    today = timezone.now().date()
    stats = {
        'total_participants': Participant.objects.count(),
        'total_events': Event.objects.count(),
        'upcoming_events': Event.objects.filter(date__gte=today).count(),
        'past_events': Event.objects.filter(date__lt=today).count(),
         
    }
    return stats

def organizer_dashboard(request):
    stats = get_dashboard_stats()
    today = timezone.now().date()
    filter_type = request.GET.get('type', 'all')

    base_query = Event.objects.select_related('category').prefetch_related('participants')

    if filter_type == 'upcoming':
        events = base_query.filter(date__gte=today)

    elif filter_type == "past":
        events = base_query.filter(date__lt=today)

    else: 
        events = base_query.all()

    
    context = {
        'stats':stats, 
        'events': events,
        'type': filter_type
    }



    return render(request, 'events/organizer_dashboard.html', context)
            
def update_event(request, id):
    event = Event.objects.get(id=id)
    form = EventForm(instance=event)
    if request.method == "POST":
        form = EventForm(request.POST, instance=event)
        if form.is_valid():
            form.save()
            messages.success(request, "Event updated successfully")

    context = {
        "form" : form
    }

    return render(request, 'events/event_form.html', context)

def delete_event(request, id):
    if request.method == "POST":
        event = Event.objects.get(id=id)
        event.delete()
        messages.success(request, "Event deleted successfully")
        return redirect ('organizer-dashboard')