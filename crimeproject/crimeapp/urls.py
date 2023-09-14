from django.contrib import admin
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('',views.index,name='index'),
    path('userregister/', views.userregister, name='userregister'),
    path('witnessregister/', views.witnessregister, name='witnessregister'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('password_reset/',auth_views.PasswordResetView.as_view(),name='password_reset'),
    path('password_reset/done/',auth_views.PasswordResetDoneView.as_view(),name='password_reset_done'),
    path('reset/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view(),name='password_reset_confirm'),
    path('reset/done/',auth_views.PasswordResetCompleteView.as_view(),name='password_reset_complete'),
    path('report_crime/', views.report_crime, name='report_crime'),
    path('reported_crimes/', views.reported_crimes, name='reported_crimes'),
    path('generate-pdf/', views.generate_pdf, name='generate_pdf'),
    # path('generate_unique_fir_number/', views.generate_unique_fir_number, name='generate_unique_fir_number'),
    path('listcrime/', views.listcrime, name='listcrime'),
    path('about/', views.about, name='about'),
    path('general/', views.general, name='general'),
    path('laws/', views.laws, name='laws'),
    path('contact/', views.contact, name='contact'),
    path('gallery/', views.gallery, name='gallery'),
    path('anony_report/', views.anony_report, name='anony_report'),
    path('anony_pdf/', views.anony_pdf, name='anony_pdf'),
]+ static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)