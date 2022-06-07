from django.urls import path
from . import views

# this like app.use() in express
urlpatterns = [
    path('', views.Home.as_view(), name="home"),
    path('about/', views.About.as_view(), name="about"),
    path('restaurantlist/', views.RestaurantList.as_view(), name="restaurant_list"),
    path('restaurantlist/new', views.RestaurantCreate.as_view(), name="restaurant_create"),
    path('restaurantlist/<int:pk>/', views.RestaurantDetail.as_view(), name="restaurant_detail"),
    # path('miles/', views.MilesList.as_view(), name="miles_list"),
]