from django.contrib import messages
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from vacapp.form import NurseForm, UserForm, HospitalForm, VaccineForm, AppointmentForm, ComplaintForm, Report_CardForm
from vacapp.models import Vaccination, Hospital, Vaccine, Appointment, Complaint, Book_Appointment, Report_Card


@login_required(login_url='login_view')
def admin_page(request):
    return render(request, 'admintemp/base.html')
@login_required(login_url='login_view')
def nurse_view(request):
    new = Vaccination.objects.filter(is_nurse=True)
    return render(request, 'admintemp/nurse_view.html', {"new": new})


@login_required(login_url='login_view')
def nurse_update(request, up):
    taskupdate = Vaccination.objects.get(id=up)
    updateform = NurseForm(instance=taskupdate)
    if request.method == 'POST':
        updateform = NurseForm(request.POST, instance=taskupdate)
        if updateform.is_valid():
            updateform.save()
            return redirect("nurse_view")
    return render(request, 'admintemp/nurse_update.html', {"updateform": updateform})


@login_required(login_url='login_view')
def nurse_delete(request, dl):
    taskdelete = Vaccination.objects.get(id=dl)
    taskdelete.delete()
    return redirect("nurse_view")


@login_required(login_url='login_view')
def user_view(request):
    new = Vaccination.objects.filter(is_user=True)
    return render(request, 'admintemp/user_view.html', {"new": new})


@login_required(login_url='login_view')
def user_update(request, up):
    taskupdate = Vaccination.objects.get(id=up)
    updateform = UserForm(instance=taskupdate)
    if request.method == 'POST':
        updateform = UserForm(request.POST, instance=taskupdate)
        if updateform.is_valid():
            updateform.save()
            return redirect("user_view")
    return render(request, 'admintemp/user_update.html', {"updateform": updateform})


@login_required(login_url='login_view')
def user_delete(request, dl):
    taskdelete = Vaccination.objects.get(id=dl)
    taskdelete.delete()
    return redirect("user_view")


@login_required(login_url='login_view')
def hospital(request):
    form = HospitalForm()
    if request.method == 'POST':
        form = HospitalForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('hospital_view')
    return render(request, 'admintemp/hospital.html', {'form': form})


@login_required(login_url='login_view')
def hospital_view(request):
    new = Hospital.objects.all()
    return render(request, 'admintemp/hospital_view.html', {"new": new})


@login_required(login_url='login_view')
def hospital_update(request, up):
    taskupdate = Hospital.objects.get(id=up)
    updateform = HospitalForm(instance=taskupdate)
    if request.method == 'POST':
        updateform = HospitalForm(request.POST, instance=taskupdate)
        if updateform.is_valid():
            updateform.save()
            return redirect("hospital_view")
    return render(request, 'admintemp/hospital_update.html', {"updateform": updateform})


@login_required(login_url='login_view')
def hospital_delete(request, dl):
    taskdelete = Hospital.objects.get(id=dl)
    taskdelete.delete()
    return redirect("hospital_view")


@login_required(login_url='login_view')
def vaccine(request):
    form = VaccineForm()
    if request.method == 'POST':
        form = VaccineForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('vaccine_view')
    return render(request, 'admintemp/vaccine.html', {'form': form})


@login_required(login_url='login_view')
def vaccine_view(request):
    new = Vaccine.objects.all()
    return render(request, 'admintemp/vaccine_view.html', {"new": new})


@login_required(login_url='login_view')
def vaccine_update(request, up):
    taskupdate = Vaccine.objects.get(id=up)
    updateform = VaccineForm(instance=taskupdate)
    if request.method == 'POST':
        updateform = VaccineForm(request.POST, instance=taskupdate)
        if updateform.is_valid():
            updateform.save()
            return redirect("vaccine_view")
    return render(request, 'admintemp/vaccine_update.html', {"updateform": updateform})


@login_required(login_url='login_view')
def vaccine_delete(request, dl):
    taskdelete = Vaccine.objects.get(id=dl)
    taskdelete.delete()
    return redirect("vaccine_view")


@login_required(login_url='login_view')
def reportcard(request, id):
    form = Book_Appointment.objects.get(id=id)
    if request.method == 'POST':
        form = Report_CardForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('reportcard_view')
    return render(request, 'admintemp/reportcard.html', {'form': form})

@login_required(login_url='login_view')
def reportcard_view(request):
    new = Report_Card.objects.all()
    return render(request, 'admintemp/reportcard_view.html', {'new': new})


@login_required(login_url='login_view')
def reportcard_update(request, up):
    taskupdate = Report_Card.objects.get(id=up)
    updateform = Report_CardForm(instance=taskupdate)
    if request.method == 'POST':
        updateform = Report_CardForm(request.POST, instance=taskupdate)
        if updateform.is_valid():
            updateform.save()
            return redirect("reportcard_view")
    return render(request, 'admintemp/reportcard_update.html', {"updateform": updateform})


@login_required(login_url='login_view')
def reportcard_delete(request, dl):
    taskdelete = Report_Card.objects.get(id=dl)
    taskdelete.delete()
    return redirect("reportcard_view")


@login_required(login_url='login_view')
def appointment_view(request):
    new = Appointment.objects.all()
    return render(request, 'admintemp/appointment_view.html', {"new": new})


@login_required(login_url='login_view')
def appointment_update(request, up):
    taskupdate = Appointment.objects.get(id=up)
    updateform = AppointmentForm(instance=taskupdate)
    if request.method == 'POST':
        updateform = AppointmentForm(request.POST, instance=taskupdate)
        if updateform.is_valid():
            updateform.save()
            return redirect("appointment_view")
    return render(request, 'admintemp/appointment_update.html', {"updateform": updateform})


@login_required(login_url='login_view')
def appointment_delete(request, dl):
    taskdelete = Appointment.objects.get(id=dl)
    taskdelete.delete()
    return redirect("appointment_view")


@login_required(login_url='login_view')
def complaint_view(request):
    new = Complaint.objects.all()
    return render(request, 'admintemp/complaint_view.html', {"new": new})


@login_required(login_url='login_view')
def complaint_update(request, up):
    taskupdate = Complaint.objects.get(id=up)
    updateform = ComplaintForm(instance=taskupdate)
    if request.method == 'POST':
        updateform = ComplaintForm(request.POST, instance=taskupdate)
        if updateform.is_valid():
            updateform.save()
            return redirect("complaint_view")
    return render(request, 'admintemp/complaint_update.html', {"updateform": updateform})


@login_required(login_url='login_view')
def complaint_delete(request, dl):
    taskdelete = Complaint.objects.get(id=dl)
    taskdelete.delete()
    return redirect("complaint_view")


@login_required(login_url='login_view')
def complaint_replay(request, id):
    form = Complaint.objects.get(id=id)
    if request.method == 'POST':
        r = request.POST.get('reply')
        print(r)
        form.replay = r
        form.save()
        return redirect('complaint_view')
    return render(request, 'admintemp/complaint_replay.html', {'form': form})

def book_appointment_view(request):
    new = Book_Appointment.objects.all()
    return render(request, 'admintemp/book_appointment_view.html', {"new": new})
def approve_appointment(request,id):
    n = Book_Appointment.objects.get(id=id)
    n.status = 1
    n.save()
    messages.info(request,'Appointment confirmed')
    return redirect('book_appointment_view')

def reject_appointment(request,id):
    n = Book_Appointment.objects.get(id=id)
    n.status = 2
    n.save()
    messages.info(request,'Appointment rejected')
    return redirect('book_appointment_view')


def vaccination_view(request):
    new = Book_Appointment.objects.filter(status=1)
    return render(request, 'admintemp/vaccination_view.html', {"new": new})

