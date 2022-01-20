from django.shortcuts import render
from django.views.generic import TemplateView

class MainView(TemplateView):
    template_name = 'main.html'
class AboutView(TemplateView):
    template_name = 'about.html'
# Create your views here.
