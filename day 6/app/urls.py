from django.urls import path
from app.views import forms_as_p,forms_for,login

urlpatterns = [
    path('',forms_as_p,name='forms'),
    path('login/',login,name='login'),
    path('forms-for/',forms_for,name='forms-for')
]