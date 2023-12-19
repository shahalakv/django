from django.shortcuts import redirect, render

from vacapp.form import AppointmentForm, ComplaintForm
from vacapp.models import Appointment, Complaint, Vaccine, Vaccination, Hospital


def vaccine_views(request):
    new = Vaccine.objects.all()
    return render(request, 'nursetemp/vaccine_views.html', {"new": new})

def user_views(request):
    new = Vaccination.objects.filter(is_user=True)
    return render(request, 'nursetemp/user_views.html', {"new": new})

def hospital_views(request):
    new = Hospital.objects.all()
    return render(request, 'nursetemp/hospital_views.html', {"new": new})


def complaints(request):
    form = ComplaintForm()
    u = request.user
    if request.method == 'POST':
        form = ComplaintForm(request.POST)
        if form.is_valid():
            ob = form.save(commit=False)
            ob.user = u
            ob.save()
        return redirect('complaint_views')
    return render(request, 'nursetemp/complaints.html', {'form': form})

def complaint_views(request):
    new = Complaint.objects.filter(user=request.user)
    return render(request, 'nursetemp/complaint_views.html', {"new": new})

def complaint_updates(request, up):
    taskupdate = Complaint.objects.get(id=up)
    updateform = ComplaintForm(instance=taskupdate)
    if request.method == 'POST':
        updateform = ComplaintForm(request.POST, instance=taskupdate)
        if updateform.is_valid():
            updateform.save()
            return redirect("complaint_views")
    return render(request, 'nursetemp/complaint_updates.html', {"updateform": updateform})

def complaint_deletes(request, dl):
    taskdelete = Complaint.objects.get(id=dl)
    taskdelete.delete()
    return redirect("complaint_views")
def complaint_replay_status(request):
    new = Complaint.objects.filter(user=request.user)
    return render(request, 'nursetemp/complaint_replay_status.html', {"new": new})
def profile_view(request):
    new = Vaccination.objects.filter(username=request.user)
    return render(request, 'nursetemp/profile_view.html', {"new": new})

def schedules(request):
    form = AppointmentForm()
    if request.method == 'POST':
        form = AppointmentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('schedules')
    return render(request, 'nursetemp/schedules.html', {'form': form})

def schedule_views(request):
    new = Appointment.objects.all()
    return render(request, 'nursetemp/schedule_views.html', {"new": new})

def schedule_updates(request, up):
    taskupdate = Appointment.objects.get(id=up)
    updateform = AppointmentForm(instance=taskupdate)
    if request.method == 'POST':
        updateform = AppointmentForm(request.POST, instance=taskupdate)
        if updateform.is_valid():
            updateform.save()
            return redirect("schedule_views")
    return render(request, 'nursetemp/schedule_updates.html', {"updateform": updateform})

def schedule_deletes(request, dl):
    taskdelete = Appointment.objects.get(id=dl)
    taskdelete.delete()
    return redirect("schedule_views")
