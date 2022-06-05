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
    path('team', views.team, name="Administration page"),
    path('convent', views.convent, name="Convents page page"),



    path('delete_slider', views.delete_slider, name="delete_slider"),
    path('slider_edit', views.slider_edit, name="slider_edit"),
    path('home_edit', views.home_edit, name="home_edit"),
    path('activities_edit', views.activities_edit, name="activities_edit"),
    path('about_edit', views.about_edit, name="about_edit"),
    path('add_slider', views.add_slider, name="add_slider"),
    path('update_contact', views.update_contact, name="update_contact"),
    path('update_logo', views.update_logo, name="update_logo"),
    path('update_identity', views.update_identity, name="update_identity"),
    path('update_patron1', views.update_patron1, name="update_patron1"),
    path('update_patron2', views.update_patron2, name="update_patron2"),
    path('update_patron3', views.update_patron3, name="update_patron3"),
    path('update_mission', views.update_mission, name="update_mission"),
    path('team_update', views.team_update, name="team_update"),
    path('publish_update', views.publish_update, name="publish_update"),
    path('gallery_category_delete', views.gallery_category_delete, name="gallery_category_delete"),
    path('add_gallery', views.add_gallery, name="New Photos in gallery"),
]
