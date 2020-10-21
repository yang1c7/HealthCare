from datetime import datetime
import pytz
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse
from myapp.forms import PatientForm, DoctorForm
from myapp.models import Topic
from django.views import View

# Create your views here.

class IndexView(View):
    def get(self, request):
        if 'last_login' in request.session:
            last_login = request.session['last_login']
        else:
            last_login = "Your last login was more than one hour ago!!"
        # top_list = Topic.objects.all().order_by('id')[:10]
        # request.session.set_test_cookie()
        return render(request, 'myapp/index.html', {'ash': self.get_queryset(), 'last_login': last_login})

    def get_queryset(self):
        return Topic.objects.all().order_by('id')[:10]

def patient(request):
    msg = ''
    if request.method == 'POST':
        form = PatientForm(request.POST)
        if form.is_valid():
            patient = form.save(commit=False)
            patient.save()
            msg = 'Your information has been uploaded successfully.'
        return render(request, 'myapp/patient_response.html', {'msg': msg})
    else:
        form = PatientForm()
    return render(request, 'myapp/patient.html', {'form': form, 'msg': msg})

def doctor(request):
    msg = ''
    if request.method == 'POST':
        form = DoctorForm(request.POST)
        if form.is_valid():
            doctor = form.save(commit=False)
            doctor.save()
            msg = 'Your feedback has been uploaded successfully.'
        return render(request, 'myapp/doctor_response.html', {'msg': msg})
    else:
        form = DoctorForm()
    return render(request, 'myapp/doctor.html', {'form': form, 'msg': msg})

def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        current_login_time = datetime.now(pytz.timezone('America/Toronto'))
        timestamp = current_login_time.strftime("%d-%b-%Y (%H:%M:%S)")
        request.session['last_login'] = 'Last Login: ' + timestamp
        request.session.set_expiry(60)
        if user:
            login(request, user)
            if 'next' in request.POST:
                return redirect(request.POST.get('next'))
            else:
                return HttpResponseRedirect(reverse('myapp:index'))
        else:
            return HttpResponse('Invalid login details.')
    else:
        return render(request, 'myapp/login.html')

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user, backend='django.contrib.auth.backends.ModelBackend')
            return redirect('myapp:index')
    else:
        form = UserCreationForm()
    return render(request, 'myapp/register.html', {'form': form})

@login_required
def user_logout(request):
    request.session.flush()
    return HttpResponseRedirect(reverse('myapp:index'))

