from django.db import models
import datetime
class Slider(models.Model):
    img=models.FileField()
    word=models.CharField(max_length=30)

class Gallery(models.Model):
    function_name = models.CharField(max_length=30)
    image= models.FileField()

class Gallery_category(models.Model):
    function_name=models.CharField(max_length=30)


class Team(models.Model):
    team_members = models.FileField()
    member_name = models.CharField(max_length=30)
    member_role = models.CharField(max_length=30)
    member_description = models.TextField()

class Publications(models.Model):
    book_description= models.TextField()
    book = models.FileField()

class Saint(models.Model):
    saint_img = models.FileField()
    saint_name = models.CharField(max_length=30)
    saint_title = models.CharField(max_length=30)


class Unique(models.Model):
    logo = models.FileField()
    identity_heading = models.TextField()
    identity_data = models.TextField()
    identity_cover = models.FileField()
    mission_data = models.TextField()
    mission_cover = models.FileField()
    location_cover = models.FileField()
    activities_description = models.TextField()


    patron1 = models.FileField()
    patron1_name = models.CharField(max_length=30)
    patron1_role = models.CharField(max_length=30)
    patron1_description = models.TextField()
    patron2 = models.FileField()
    patron2_name = models.CharField(max_length=30)
    patron2_role = models.CharField(max_length=30)
    patron2_description = models.TextField()
    patron3 = models.FileField()
    patron3_name = models.CharField(max_length=30)
    patron3_role = models.CharField(max_length=30)
    patron3_description = models.TextField()

class Activities(models.Model):
    category = models.CharField(max_length=30)
    image = models.FileField()
    name = models.CharField(max_length=30)
    place = models.CharField(max_length=30)

class Activities_category(models.Model):
    category = models.CharField(max_length=30)


class About(models.Model):
    abt1_description = models.TextField()
    abt1_cover = models.FileField()
    abt2_heading = models.CharField(max_length=100)
    abt2_description = models.TextField()
    abt3_heading= models.CharField(max_length=100)
    abt3_description = models.TextField()

class Contact(models.Model):
    code = models.IntegerField()
    phn1 = models.IntegerField()
    phn2 = models.IntegerField()
    address = models.TextField()
    pin = models.IntegerField()
    email = models.CharField(max_length=30)

class Event(models.Model):
    event_title = models.CharField(max_length=30)
    event_day = models.CharField(max_length=30)
    event_venue = models.CharField(max_length=30)
    event_description = models.TextField()
    event_img1 = models.FileField()
    event_img2 = models.FileField()


















