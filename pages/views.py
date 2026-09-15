from django.shortcuts import render
from services.models import Service
from .models import FAQ
from .models import Slider

def index(request):
    all_services = Service.objects.filter(is_active=True).order_by('order', 'name')
    sliders = Slider.objects.filter(is_active=True).order_by('order')
    return render(request, 'index.html', {
        'all_services': all_services,
        'sliders': sliders,  
    })

def contacts_view(request):
    return render(request, 'contacts.html')

def about_view(request):
    return render(request, 'about.html')

def faq_view(request):
    faqs = FAQ.objects.filter(is_active=True).order_by('order', 'question')
    return render(request, 'faq.html', {'faqs': faqs})