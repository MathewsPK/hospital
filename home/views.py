from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import doctors,departments,appointments
from .forms import AppointmentForm
def home(request):
    return render(request,'index.html')
def Doctors(request):
    dict_doc = {
        'doc': doctors.objects.all()
    }
    return render(request, 'doctors.html', dict_doc)
def Appointment(request):
    dict_doc = doctors.objects.all()
    dict_dep = departments.objects.all()

    if request.method == 'POST':
        form = AppointmentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('Confirmation')
            # Redirect to a success page or another URL if needed.

    else:
        form = AppointmentForm()

    context = {
        'doc': dict_doc,
        'dep': dict_dep,
        'form': form,
    }

    return render(request, 'appointment.html', context)

def Department(request):
    dict_dep ={
        'dep' : departments.objects.all()
    }
    return render(request,'department.html',dict_dep)
def Confirmation(request):
    return render(request, 'confirmation.html')

