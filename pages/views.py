from django.shortcuts import render
from django.views.generic import TemplateView

class MainPageView(TemplateView):
    template_name="pages/main.html"
# Create your views here.
