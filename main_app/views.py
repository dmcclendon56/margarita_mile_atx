from django.shortcuts import render
from django.views import View
from django.http import HttpResponse
from django.views.generic.base import TemplateView
from django.shortcuts import redirect

from django.views.generic import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from main_app.models import Restaurant, Miles, Default

from django.urls import reverse

# Create your views here.

class Home(View):
    def get(self, request):
        return HttpResponse("Margartia Mile Home")

class About(View):
    def get(self, request):
        return HttpResponse("Margarita Mile About")


class Home(TemplateView):
    template_name = "home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["miles"] = Miles.objects.all() 
        context['default_miles']= Default.objects.all()
        return context



class About(TemplateView):
    template_name = "about.html"


class MileList(TemplateView):
    template_name = "mile_list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["miles"] = Miles.objects.all() 
        return context

class MileDetail(DetailView):
    model = Miles
    template_name = "mile_detail.html"   

class MileCreate(CreateView):
    model = Miles
    fields = ['title', 'img']
    template_name = "mile_create.html"
    success_url = "/milelist/" 


class MileDelete(DeleteView):
    model = Miles
    template_name = "mile_delete_.html"
    success_url = "/milelist/"

class MileUpdate(UpdateView):
    model = Miles
    fields = ['name', 'img']
    template_name = "mile_update.html"  
    

    def get_success_url(self):
        return reverse('restaurant_detail', kwargs={'pk': self.object.pk})    


class NorthMile(DetailView):
    def get(self, request):
        return HttpResponse("Margarita Mile-North")
    

class CentralMile(DetailView):
    def get(self, request):
        return HttpResponse("Margarita Mile-Central")

class SouthMile(DetailView):
    def get(self, request):
        return HttpResponse("Margarita Mile-South")        


class RestuarantList(TemplateView):
    template_name = "restaurant_list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["miles"] = Miles.objects.all() 
        return context

# class RestaurantCreate(CreateView):
#     model = Restaurant
#     fields = ['restaurant', 'img', 'margarita', 'price', 'miles' ]
#     template_name = "restaurant_create.html"
#     success_url = "/restaurantlist/" 

class RestaurantCreate(View):

    def post(self, request, pk):
        restaurant = request.POST.get("restaurant")
        img = request.POST.get("img")
        margarita = request.POST.get("margarita")
        price = request.POST.get("price")
        mile = Miles.objects.get(pk=pk)
        Restaurant.objects.create(restaurant=restaurant, img=img, margarita=margarita, price = price, mile=mile)
        
        return redirect('mile_detail', pk=pk)    
      