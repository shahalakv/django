from django.core.checks import messages
from django.shortcuts import redirect, render

from vacapp.admin_views import vaccine
from vacapp.form import ComplaintForm, AppointmentForm
from vacapp.models import Complaint, Appointment, Reportcard, Vaccination, Book_Appointment, Vaccine


def schedule_viewz(request):
    new = Appointment.objects.all()
    return render(request, 'usertemp/schedule_viewz.html', {"new": new})

def complaintz(request):
    form = ComplaintForm()
    u = request.user
    if request.method == 'POST':
        form = ComplaintForm(request.POST)
        if form.is_valid():
            ob = form.save(commit=False)
            ob.user = u
            ob.save()
        return redirect('complaint_viewz')
    return render(request, 'usertemp/complaintz.html', {'form': form})

def complaint_viewz(request):
    new = Complaint.objects.filter(user=request.user)
    return render(request, 'usertemp/complaint_viewz.html', {"new": new})

def complaint_updatez(request, up):
    taskupdate = Complaint.objects.get(id=up)
    updateform = ComplaintForm(instance=taskupdate)
    if request.method == 'POST':
        updateform = ComplaintForm(request.POST, instance=taskupdate)
        if updateform.is_valid():
            updateform.save()
            return redirect("complaint_viewz")
    return render(request, 'usertemp/complaint_updatez.html', {"updateform": updateform})

def complaint_deletez(request, dl):
    taskdelete = Complaint.objects.get(id=dl)
    taskdelete.delete()
    return redirect("complaint_viewz")
def complaint_status(request):
    new = Complaint.objects.filter(user=request.user)
    return render(request, 'usertemp/complaint_status.html', {"new": new})

def reportcard_viewz(request):
    new = Reportcard.objects.all()
    return render(request, 'usertemp/reportcard_viewz.html', {'new': new})
def profile(request):
    new = Vaccination.objects.filter(username=request.user)

    return render(request, 'usertemp/profile.html', {"new": new})

def book_appointment(request, id):
    schedule = Appointment.objects.get(id=id)
    data = request.user
    vaccine_name = Vaccine.objects.get(id=id)
    print(data)
    # u = Vaccination.objects.get(user=data)
    appointment = Book_Appointment.objects.filter(user_id=id, schedule=schedule)
    if appointment.exists():
        # messages.info(request, 'you have already requested appointment for this schedule')
        return redirect('schedule_viewz')
    else:
        if request.method == 'POST':
            obj = Book_Appointment()
            obj.user = data
            obj.schedule = schedule
            obj.vaccine_name = vaccine_name
            obj.save()
            return redirect('schedule_viewz')
    return render(request, 'usertemp/book_appointment.html', {'schedule': schedule})