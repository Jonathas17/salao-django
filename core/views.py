from django.shortcuts import render, redirect, get_object_or_404
from .models import Service, Stylist, GalleryImage
from .forms import ClientForm, AppointmentForm

def home(request):
    services = Service.objects.all()
    stylists = Stylist.objects.filter(active=True)
    gallery = GalleryImage.objects.order_by('-created_at')[:6]
    return render(request, 'core/home.html', {'services': services, 'stylists': stylists, 'gallery': gallery})

def service_detail(request, pk):
    service = get_object_or_404(Service, pk=pk)
    return render(request, 'core/service_detail.html', {'service': service})

def book_appointment(request):
    if request.method == 'POST':
        client_form = ClientForm(request.POST)
        appt_form = AppointmentForm(request.POST)
        if client_form.is_valid() and appt_form.is_valid():
            client = client_form.save()
            appt = appt_form.save(commit=False)
            appt.client = client
            appt.save()
            return render(request, 'core/booking_success.html', {'appointment': appt})
    else:
        client_form = ClientForm()
        appt_form = AppointmentForm()
    return render(request, 'core/book_appointment.html', {'client_form': client_form, 'appt_form': appt_form})
