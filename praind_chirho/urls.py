from django.urls import path

from .views import *
from . import views

urlpatterns = [
    path('about_chirho/', views.AboutUsChirho.as_view(), name="about_chirho"),
    path('brigadas_chirho/', views.BrigadasChirho.as_view(), name="brigadas_chirho"),
    path('certifications_chirho/', MaquinariaEquipoCreateChirho.as_view(), name="maquinariaequipo_chirho"),
    path('contact_chirho/', views.ContactUsChirho.as_view(), name="contact_chirho"),
    path('', views.PraindIndexChirho.as_view(), name="index_chirho"),
    path('services_chirho/', views.ServicesChirho.as_view(), name="services_chirho"),
    path('training_chirho', views.EntrenamientosCreateChirho.as_view(), name="training_chirho"),
    path('equipo_list_chirho', views.MaquinariaEquipoListChirho.as_view(), name="equipo_list_chirho"),
    path('cursos_list_chirho', views.EntrenamientosListChirho.as_view(), name="cursos_list_chirho"),

]