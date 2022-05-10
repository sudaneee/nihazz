from django.urls import path
from . import views


urlpatterns = [
    path('', views.form_home, name='form-home'),
    path('apply', views.application_form, name='application-form'),
]