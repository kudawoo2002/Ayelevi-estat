from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('', views.index, name='index'),
    path('properties/', views.property, name='property'),
    path('property/detail/<slug:house_slug>/', views.house_detail, name='house_detail'),
    path('property/houses/location/<slug:location_slug>/', views.house_by_location, name='house_by_location'),
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
