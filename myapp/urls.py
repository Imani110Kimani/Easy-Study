from django.contrib import admin
from django.urls import path
from myapp import views  # Import your views

urlpatterns = [
    path('index/', views.index, name='index'),  # Root URL mapped to the index view
    path('', views.register, name='register'),  # This maps the root to the register view
    path('login/', views.login, name='login'),

    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('courses/', views.courses, name='courses'),
    path('seecourse/', views.seecourse, name='seecourse'),
    path('events/', views.events, name='events'),
    path('pricing/', views.pricing, name='pricing'),
    path('starter/', views.starter, name='starter'),
    path('trainers/', views.trainers, name='trainers'),
    path('web_dev/', views.web_dev, name='web_dev'),
    path('search_engine/', views.search_engine, name='search_engine'),
    path('copy_write/', views.copy_write, name='copy_write'),
    path('pay/', views.pay, name='pay'),
    path('payment/process/', views.process_payment, name='process_payment'),
    path('show_contacts/', views.show_contacts, name='show_contacts'),
    path('delete_contact/<int:id>', views.delete_contact),
    path('edit_contact/<int:id>', views.edit_contact),
    path('update_contact/<int:id>', views.update_contact, name='update_contact'),



]

