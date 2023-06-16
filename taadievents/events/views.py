from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, get_object_or_404
from .models import Event

def event_list(request):
    
    events = Event.objects.all()
    return render(request, 'event_list.html', {'events': events})

def event_detail(request, event_id):
    event = get_object_or_404(Event, pk=event_id)
    return render(request, 'event_detail.html', {'event': event})