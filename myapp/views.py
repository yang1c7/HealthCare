from datetime import datetime
import pytz
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from myapp.forms import UserCreationForm
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse
from myapp.forms import PatientForm, DoctorForm
from myapp.models import Topic, Patient
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


def home(request):

    return render(request, 'myapp/home.html')


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


def account(request):
    return render(request, 'myapp/account.html')


def userInfoChange(request):
    if request.method == 'POST':
        form_obj = PatientForm(request.POST)
        #print(form_obj)
        if form_obj.is_valid():
            id = request.POST.get("id", "")
            patient = Patient.objects.filter(user_id=id)
            _patient = patient[0]
            oldUser = User.objects.filter(id=id)
            _oldUser = oldUser[0]

            username = request.POST.get("username", "")
            check = True
            if username:
                checkifUsername = User.objects.filter(username=username)
                if checkifUsername.count() != 0:
                    check = False
                else:
                    _patient.username = username
                    _oldUser.username = username
            email = request.POST.get("email", "")
            if email:
                _patient.email = email
                _oldUser.email = email
            first_name = request.POST.get("first_name", "")
            if first_name:
                _patient.first_name = first_name
                _oldUser.first_name = first_name
            last_name = request.POST.get("last_name", "")
            if last_name:
                _patient.last_name = last_name
                _oldUser.last_name = last_name
            age = request.POST.get("age", "")
            if age:
                _patient.age = age
            gender = request.POST.get("gender", "")
            if gender:
                if gender == 'M':
                    _patient.gender = "M"
                    g = "Male"
                elif gender == "F":
                    _patient.gender = "F"
                    g = "Female"
            address = request.POST.get("address", "")
            if address:
                _patient.address = address

            if not check:
                return render(request, "myapp/account.html",
                              {'username': _patient.username, 'email': _oldUser.email, 'userId': id,
                               "firstname": _patient.first_name, "lastname": _patient.last_name,
                               "age": _patient.age, "gender": g, "address": _patient.address, "failed": 1})
            else:
                _patient.save()
                _oldUser.save()

                return render(request, "myapp/account.html", {'username': _patient.username, 'email': _oldUser.email, 'userId': id, "firstname": _patient.first_name, "lastname": _patient.last_name,
                                                              "age": _patient.age, "gender": g, "address": _patient.address, "failed": 0})
    return render(request, "myapp/account.html")


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
            # if 'next' in request.POST:
            #     return redirect(request.POST.get('next'))
            # else:
            patient = Patient.objects.filter(user_id=user.id)
            message = 'click to update'
            if patient.count() != 0:
                    if patient[0].first_name:
                        firstname = patient[0].first_name
                    else:
                        firstname = message
                    if patient[0].last_name:
                        lastname = patient[0].last_name
                    else:
                        lastname = message
                    if patient[0].age:
                        age = patient[0].age
                    else:
                        age = message
                    if patient[0].address:
                        address = patient[0].address
                    else:
                        address = message
                    if patient[0].gender == 'M':
                        gender = "Male"
                    elif patient[0].gender == 'F':
                        gender = "Female"
                    else:
                        gender = message
            else:
                    firstname = message
                    lastname = message
                    age = message
                    gender = message
                    address = message
            return render(request, 'myapp/account.html', {'username': user.username, 'email': user.email,
                                                              'userId': user.id, "firstname": firstname, "lastname": lastname,
                                                              "age":age, "gender": gender, "address": address})
        else:
            return render(request, 'myapp/login.html', {'msg': True})
    else:
        return render(request, 'myapp/login.html', {'msg': False})


# def register(request):
#     if request.method == 'POST':
#         form = UserCreationForm(request.POST)
#         if form.is_valid():
#             user = form.save()
#             #login(request, user, backend='django.contrib.auth.backends.ModelBackend')
#             return redirect('myapp:user_login')


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            id = user.id
            username = user.username
            p = Patient(user_id=id, username=username)
            p.save()
            #login(request, user, backend='django.contrib.auth.backends.ModelBackend')
            return redirect('myapp:user_login')
        else:
            print("is not valid")
            return render(request, 'myapp/register0.html', {"error": 1})
    return render(request, 'myapp/register0.html', {"error": 0})

@login_required
def user_logout(request):
    request.session.flush()
    return HttpResponseRedirect(reverse('myapp:home'))

