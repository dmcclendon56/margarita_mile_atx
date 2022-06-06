from django.shortcuts import render
from django.views import View
from django.http import HttpResponse
from django.views.generic.base import TemplateView

# Create your views here.

class Home(View):
    def get(self, request):
        return HttpResponse("Margartia Mile Home")


class About(View):
    def get(self, request):
        return HttpResponse("Margarita Mile About")


class Home(TemplateView):
    template_name = "home.html"



class About(TemplateView):
    template_name = "about.html"



class Mile(TemplateView):
    def get(self,request):

        return HttpResponse("Mile")