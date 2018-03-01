from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView

# Create your views here.
class IndexView(TemplateView):
	template_name = 'index.html'

class AboutPageView(TemplateView):
	template_name = 'about.html'

def index(request):
	return HttpResponse("Hola!!")