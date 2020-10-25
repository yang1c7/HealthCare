from django.contrib import admin
from django.urls import path
from django.conf.urls import include
from django.conf.urls import *
from django.contrib.auth import views as auth_views
from myapp import views

app_name = 'myapp'

urlpatterns = [
    path(r'', views.IndexView.as_view(), name='index'),
    path('admin/', admin.site.urls),
    path(r'home',views.home, name='home'),
    path(r'patient', views.patient, name='patient'),
    path(r'patient_response', views.patient, name='patient_response'),
    path(r'doctor', views.doctor, name='doctor'),
    path(r'doctor_response', views.doctor, name='doctor_response'),
    path(r'login', views.user_login, name='user_login'),
    path(r'logout', views.user_logout, name='user_logout'),
    path(r'register', views.register, name='register'),

    path(r'accounts/', include('django.contrib.auth.urls')),
    path(r'password_change/done/',
         auth_views.PasswordChangeDoneView.as_view(template_name='registration/password_change_done.html'),
         name='password_change_done'),

    path(r'password_change/', auth_views.PasswordChangeView.as_view(template_name='registration/password_change.html'),
         name='password_change'),

    path(r'password_reset/done/',
         auth_views.PasswordResetCompleteView.as_view(template_name='registration/password_reset_done.html'),
         name='password_reset_done'),

    path(r'reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path(r'password_reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),

    path(r'reset/done/',
         auth_views.PasswordResetCompleteView.as_view(template_name='registration/password_reset_complete.html'),
         name='password_reset_complete'),


]
