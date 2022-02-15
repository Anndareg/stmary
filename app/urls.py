from django.urls import path
from .import views

urlpatterns = [
    path('', views.index,name="index"),
    path('index', views.index,name="index"),
    path('publications', views.publications,name="publications"),
    path('about', views.about,name="about"),
    path('activities', views.activities,name="activities"),
    path('contact', views.contact, name="contact"),
    path('gallery', views.gallery, name="gallery"),
    path('events', views.events, name="events"),
    path('gallerysingle', views.gallerysingle, name="gallerysingle"),
    path('activitysingle', views.activitysingle, name="activitysingle"),
    path('adminn', views.adminn, name="adminn"),

]
