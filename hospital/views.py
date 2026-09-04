from django.shortcuts import render,redirect
from datetime import date
from .models import Patient, Doctor, Appointment


def home(request):

    patient_count = Patient.objects.count()
    doctor_count = Doctor.objects.count()
    appointment_count = Appointment.objects.count()
    today = date.today()

    context = {
        'patient_count': patient_count,
        'doctor_count': doctor_count,
        'appointment_count': appointment_count,
        'today': today,
    }

    return render(request, 'hospital/home.html', context)


def patients(request):

    patients = Patient.objects.all()

    return render(
        request,
        'hospital/patients.html',
        {'patients': patients}
    )


def doctors(request):

    doctors = Doctor.objects.all()

    return render(
        request,
        'hospital/doctors.html',
        {'doctors': doctors}
    )


def appointments(request):

    appointments = Appointment.objects.all()

    return render(
        request,
        'hospital/appointments.html',
        {'appointments': appointments}
    )

def reports(request):

    patient_count = Patient.objects.count()
    doctor_count = Doctor.objects.count()
    appointment_count = Appointment.objects.count()

    context = {
        'patient_count': patient_count,
        'doctor_count': doctor_count,
        'appointment_count': appointment_count,
    }

    return render(
        request,
        'hospital/reports.html',
        context
    )

def add_patient(request):

    if request.method == 'POST':

        name = request.POST['name']
        age = request.POST['age']
        disease = request.POST['disease']

        Patient.objects.create(
            name=name,
            age=age,
            disease=disease
        )

        return redirect('patients')

    return render(request, 'hospital/add_patient.html')

def add_doctor(request):

    if request.method == 'POST':

        name = request.POST['name']
        specialization = request.POST['specialization']

        Doctor.objects.create(
            name=name,
            specialization=specialization
        )

        return redirect('doctors')

    return render(request, 'hospital/add_doctor.html')