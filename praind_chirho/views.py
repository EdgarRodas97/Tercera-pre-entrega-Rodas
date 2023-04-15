from django.shortcuts import render
from django.views.generic import CreateView, ListView, UpdateView, TemplateView
from django.urls import reverse
from .models import EntrenamientosChirho, MaquinariaEquipoChirho
from .forms import EntrenamientosFormChirho, MaquinariaEquipoFormChirho
from django.contrib import messages
from django.db.models import Q


class PraindIndexChirho(TemplateView):
    template_name = "index_chirho.html"


class ServicesChirho(TemplateView):
    template_name = "services_chirho.html"


class MaquinariaEquipoCreateChirho(CreateView):
    template_name = "maquinaria_equipo_chirho.html"
    form_class = MaquinariaEquipoFormChirho

    def form_valid(self, form_chirho):
        if form_chirho.is_valid():
            form_chirho.nombre_chirho = form_chirho.cleaned_data['nombre_chirho']
            form_chirho.modelo_chirho = form_chirho.cleaned_data['modelo_chirho']
            form_chirho.save()
        else:
            pass
        return super().form_valid(form_chirho)
    
    def get_success_url(self, *args_chirho, **kwargs_chirho):
        messages.info(self.request, 'Exito al guardar entrenamiento')
        url_chirho = reverse('maquinariaequipo_chirho')
        return url_chirho

class MaquinariaEquipoListChirho(ListView):
    template_name = "equipo_list_chirho.html"
    model = MaquinariaEquipoChirho
     
    def get_context_data(self, *args, **kwargs):
        context_chirho = super().get_context_data(**kwargs)
        q_chirho = self.request.GET.get("q_chirho", None)
        context_chirho['q_chirho'] = q_chirho
        return context_chirho

    def get_queryset(self, **kwargs):
        equipos_chirho = []
        q_chirho = self.request.GET.get("q_chirho", None)
        if q_chirho:
            equipos_chirho = MaquinariaEquipoChirho.objects.filter(
                Q(nombre_chirho__icontains=q_chirho) |
                Q(modelo_chirho__icontains=q_chirho) )
        return equipos_chirho



class EntrenamientosCreateChirho(CreateView):
    template_name = "entrenamientos_chirho.html"
    form_class = EntrenamientosFormChirho

    def form_valid(self, form_chirho):
        if form_chirho.is_valid():
            form_chirho.nombrecurso_chirho = form_chirho.cleaned_data['nombrecurso_chirho']
            form_chirho.save()
        else:
            pass
        return super().form_valid(form_chirho)
    
    def get_success_url(self, *args_chirho, **kwargs_chirho):
        messages.info(self.request, 'Exito al guardar entrenamiento')
        url_chirho = reverse('training_chirho')
        return url_chirho

class EntrenamientosListChirho(ListView):
    template_name = "entrenamientos_list_chirho.html"
    model = EntrenamientosChirho
     
    def get_context_data(self, *args, **kwargs):
        context_chirho = super().get_context_data(**kwargs)
        q_chirho = self.request.GET.get("q_chirho", None)
        context_chirho['q_chirho'] = q_chirho
        return context_chirho

    def get_queryset(self, **kwargs):
        cursos_chirho = []
        q_chirho = self.request.GET.get("q_chirho", None)
        if q_chirho:
            cursos_chirho = EntrenamientosChirho.objects.filter(nombrecurso_chirho__icontains=q_chirho )
        return cursos_chirho



class BrigadasChirho(TemplateView):
    template_name = "brigadas_chirho.html"


class AboutUsChirho(TemplateView):
    template_name = "about_chirho.html"


class ContactUsChirho(TemplateView):
    template_name = "contact_chirho.html"




    
