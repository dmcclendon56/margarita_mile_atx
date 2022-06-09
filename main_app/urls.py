from django.urls import path
from . import views

# this like app.use() in express
urlpatterns = [
    path('', views.Home.as_view(), name="home"),
    path('about/', views.About.as_view(), name="about"),
    path('milelist/', views.MileList.as_view(), name="mile_list"),
    path('milelist/new', views.MileCreate.as_view(), name="mile_create"),
    path('milelist/<int:pk>/', views.MileDetail.as_view(), name="mile_detail"),
    path('milelist/<int:pk>/update', views.MileUpdate.as_view(), name="mile_update"),
    path('milelist/<int:pk>/delete', views.MileDelete.as_view(), name="mile_delete"),
    path('northmile/', views.NorthMile.as_view(), name="north_mile"),
    path('centralmile/', views.CentralMile.as_view(), name="central_mile"),
    path('southmile/', views.SouthMile.as_view(), name="south_mile"),
    path('milelist/<int:pk>/restaurantlist/new', views.RestaurantCreate.as_view(), name="restaurant_list"),

]