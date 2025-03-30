from django.shortcuts import render
from django.views.generic import TemplateView

# Class-based views replacing function-based views
class HomeView(TemplateView):
    template_name = 'mango_app/home.html'

class PestsView(TemplateView):
    template_name = 'mango_app/pests.html'

class DiseasesView(TemplateView):
    template_name = 'mango_app/diseases.html'

class SurveillanceView(TemplateView):
    template_name = 'mango_app/surveillance.html'

class AboutView(TemplateView):
    template_name = 'mango_app/about.html'