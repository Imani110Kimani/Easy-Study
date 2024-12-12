from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
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
    path('show_contacts/', views.show_contacts, name='show_contacts'),
    path('delete_contact/<int:id>', views.delete_contact),
    path('edit_contact/<int:id>', views.edit_contact),
    path('update_contact/<int:id>', views.update_contact, name='update_contact'),
    path('trainers/', views.trainers, name='trainers'),
    path('upload_trainer/', views.upload_trainer, name='upload_trainer'),
    path('show_image/', views.show_image, name='show_image'),
    path('admin_dashboard/', views.admin_dashboard, name='admin_dashboard'),
    path('course-payment/', views.course_payment, name='course_payment'),
    path('start-study/', views.start_study, name='start_study'),

]

# Add this line to serve media files during development
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
