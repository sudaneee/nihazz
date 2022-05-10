from django.shortcuts import render
from .models import (
    Slider,
    GeneralSettings,
    Program,
    Update,
    Event,
)

# Create your views here.
def home(request):

    slider = Slider.objects.all()
    settings = GeneralSettings.objects.all()
    programs = Program.objects.all()
    updates = Update.objects.all()
    events = Event.objects.all() 
    
    context = {
        'slider': slider,
        'settings': settings,
        'programs': programs,
        'updates': updates,
        'events': events,

    }

    return render(request, 'website/index.html', context)