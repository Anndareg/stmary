from django.shortcuts import render
from .models import Slider
from.models import Gallery
from.models import Unique
from.models import Team
from.models import Saint
from.models import Publications
from .models import Activities
from .models import About
from .models import Contact
from .models import Gallery_category
from .models import Activities_category



def index(request):
    abt = About.objects.all()
    slider=Slider.objects.all()
    pic= Gallery.objects.all()
    fixed = Unique.objects.all()
    members = Team.objects.all()
    saint = Saint.objects.all()
    publish = Publications.objects.all()
    cnt = Contact.objects.all()
    return render(request,'index.html',{'abt':abt,'pic':pic,'fixed':fixed,'members':members,'saint':saint,'publish':publish,'slider':slider,'cnt':cnt})

def events(request):
    slider = Slider.objects.all()
    fixed = Unique.objects.all()
    cnt = Contact.objects.all()
    abt = About.objects.all()
    return render(request, 'events.html',{'slider':slider,'fixed':fixed,'cnt':cnt,'abt':abt})


def publications(request):
    abt = About.objects.all()
    slider=Slider.objects.all()
    fixed = Unique.objects.all()
    publish = Publications.objects.all()
    cnt = Contact.objects.all()
    return render(request,'publications.html',{'abt':abt,'fixed':fixed,'publish':publish,'slider':slider,'cnt':cnt})


def activities(request):
    abt = About.objects.all()
    slider = Slider.objects.all()
    activity = Activities.objects.all()
    fixed = Unique.objects.all()
    cnt = Contact.objects.all()
    act_category=Activities_category.objects.all()
    return render(request,'activities.html',{'abt':abt,'fixed':fixed,'activity':activity,'slider':slider,'cnt':cnt,'act_category':act_category})

def activitysingle(request):
    abt = About.objects.all()
    slider = Slider.objects.all()
    activity = Activities.objects.all()
    fixed = Unique.objects.all()
    cnt = Contact.objects.all()
    act_category=Activities_category.objects.all()
    id = request.POST['id']
    p = Activities_category.objects.get(id=id)
    print(id)
    r = Activities.objects.filter(category=p.category)
    return render(request,'activitysingle.html',{'abt':abt,'fixed':fixed,'activity':activity,'slider':slider,'cnt':cnt,'act_category':act_category,'r':r})



def about(request):
    slider = Slider.objects.all()
    fixed = Unique.objects.all()
    abt = About.objects.all()
    cnt = Contact.objects.all()
    pic = Gallery.objects.all()
    return render(request,'about.html',{'abt':abt,'fixed':fixed,'abt':abt,'slider':slider,'cnt':cnt,'pic':pic})

def contact(request):
    abt = About.objects.all()
    slider = Slider.objects.all()
    fixed = Unique.objects.all()
    cnt = Contact.objects.all()
    return render(request,'contact.html',{'abt':abt,'fixed':fixed,'slider':slider,'cnt':cnt})

def gallery(request):
    fixed = Unique.objects.all()
    abt = About.objects.all()
    slider = Slider.objects.all()
    pic = Gallery.objects.all()
    cnt = Contact.objects.all()
    cat = Gallery_category.objects.all()
    return render(request,'gallery.html',{'abt':abt,'pic':pic,'slider':slider,'cnt':cnt,'cat':cat,'fixed':fixed})

def gallerysingle(request):
    fixed = Unique.objects.all()
    abt = About.objects.all()
    slider = Slider.objects.all()
    pic = Gallery.objects.all()
    cnt = Contact.objects.all()
    cat = Gallery_category.objects.all()
    id = request.POST['id']
    p = Gallery_category.objects.get(id=id)
    print(id)
    r = Gallery.objects.filter(function_name=p.function_name)
    return render(request, 'gallerysingle.html', {'abt': abt, 'pic': pic, 'slider': slider, 'cnt': cnt, 'cat': cat,'r':r,'fixed':fixed})

def adminn(request):
    return render(request, 'adminn.html')

def slider_edit(request):
    slider = Slider.objects.all()
    cnt = Contact.objects.all()
    fixed = Unique.objects.all()
    return render(request, 'slider_edit.html',{'cnt': cnt,'slider': slider,'fixed':fixed})

def home_edit(request):
    slider = Slider.objects.all()
    cnt = Contact.objects.all()
    fixed = Unique.objects.all()
    cat = Gallery_category.objects.all()
    return render(request, 'home_edit.html',{'cnt': cnt,'slider': slider,'fixed':fixed,'cat': cat})
