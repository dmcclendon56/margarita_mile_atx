from django.shortcuts import render
from django.views import View
from django.http import HttpResponse
from django.views.generic.base import TemplateView

from django.views.generic import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from main_app.models import Restaurant

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



class About(TemplateView):
    template_name = "about.html"


class RestaurantList(TemplateView):
    template_name = "restaurant_list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["restaurant"] = Restaurant.objects.all() 
        return context

class RestaurantDetail(DetailView):
    model = Restaurant
    template_name = "restaurant_detail.html"   

class RestaurantCreate(CreateView):
    model = Restaurant
    fields = ['name', 'img', 'margarita', 'price']
    template_name = "restaurant_create.html"
    success_url = "/restaurantlist/" 


class RestaurantDelete(DeleteView):
    model = Restaurant
    template_name = "restaurant_delete_confirm.html"
    success_url = "/restaurantlist/"

class RestaurantUpdate(UpdateView):
    model = Restaurant
    fields = ['name', 'img', 'margarita', 'cost']
    template_name = "restaurant_update.html"  
    

    def get_success_url(self):
        return reverse('restaurant_detail', kwargs={'pk': self.object.pk})    





# class MilesList(TemplateView):
#     def __init__(self, restaurant, image, margarita, price):
#         self.restaurant = restaurant
#         self.image = image
#         self.margarita = margarita
#         self.price = price


      