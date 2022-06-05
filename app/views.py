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
from .models import Convents
from .models import Convent_countries
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
    return render(request,'index.html', {'abt':abt, 'pic':pic, 'fixed':fixed, 'members':members, 'saint':saint, 'publish':publish,'slider':slider,'cnt':cnt})

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

def team(request):
    slider = Slider.objects.all()
    fixed = Unique.objects.all()
    cnt = Contact.objects.all()
    pic = Gallery.objects.all()
    abt = About.objects.all()
    return render(request, 'team.html',{'abt':abt,'fixed': fixed, 'slider': slider, 'cnt': cnt,
                                        'pic': pic})

def convent(request):
    slider = Slider.objects.all()
    fixed = Unique.objects.all()
    cnt = Contact.objects.all()
    pic = Gallery.objects.all()
    abt = About.objects.all()
    convents = Convents.objects.all()
    countries = Convent_countries.objects.all()
    return render(request, 'convent.html', {'abt': abt, 'fixed': fixed, 'slider': slider, 'cnt': cnt, 'pic': pic, 'convents': convents, 'countries': countries})



def about(request):
    slider = Slider.objects.all()
    fixed = Unique.objects.all()
    abt = About.objects.all()
    cnt = Contact.objects.all()
    pic = Gallery.objects.all()
    return render(request, 'about.html', {'abt': abt, 'fixed': fixed, 'slider': slider, 'cnt': cnt, 'pic': pic})

def contact(request):
    abt = About.objects.all()
    slider = Slider.objects.all()
    fixed = Unique.objects.all()
    cnt = Contact.objects.all()
    return render(request,'contact.html',{'abt': abt, 'fixed': fixed, 'slider': slider, 'cnt': cnt})

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
    pic = Gallery.objects.all()
    cnt = Contact.objects.all()
    fixed = Unique.objects.all()
    cat = Gallery_category.objects.all()
    members = Team.objects.all()
    publish = Publications.objects.all()
    return render(request, 'home_edit.html',{'cnt': cnt,'slider': slider,'fixed':fixed,'cat': cat,'pic':pic,'members':members,'publish':publish})

def activities_edit(request):
    activity = Activities.objects.all()
    return render(request,'activities_edit.html',{'activity':activity})

def about_edit(request):
    abt = About.objects.all()
    return render(request,'about_edit.html',{'abt':abt})

def add_slider(request):
    a = request.FILES['img']
    b= request.POST['word']
    slider=Slider.objects.all()
    data=Slider(img=a,word=b);
    data.save();
    return render(request, 'slider_edit.html',{'slider': slider})

def update_contact(request):
    id = request.POST['id']
    a= request.POST['code']
    b = request.POST['phn1']
    c = request.POST['phn2']
    d = request.POST['address']
    e = request.POST['email']
    Contact.objects.filter(id=id).update(code=a,phn1=b,phn2=c,address=d,email=e);
    cnt = Contact.objects.all()
    fixed = Unique.objects.all()
    slider = Slider.objects.all()
    return render(request, 'slider_edit.html', {'slider': slider, 'fixed':fixed, 'cnt': cnt})


def delete_slider(request):
    id = request.POST['id']
    data = Slider.objects.get(id=id)
    data.delete()
    slider = Slider.objects.all()
    fixed = Unique.objects.all()
    cnt = Contact.objects.all()
    return render(request,'slider_edit.html',{'slider': slider, 'fixed':fixed, 'cnt': cnt})

def update_logo(request):
    id = request.POST['id']
    a = request.FILES['logo']
    Unique.objects.filter(id=id).update(logo=a);
    fixed = Unique.objects.all()
    slider = Slider.objects.all()
    cnt = Contact.objects.all()
    return render(request, 'slider_edit.html', {'slider': slider, 'fixed':fixed, 'cnt': cnt})

def update_identity(request):
    id = request.POST['id']
    try:
        a = request.FILES['identity_cover']
        b = request.POST['identity_heading']
        c = request.POST['identity_data']
        Unique.objects.filter(id=id).update(identity_cover=a,identity_heading=b,identity_data=c);
        slider = Slider.objects.all()
        pic = Gallery.objects.all()
        cnt = Contact.objects.all()
        fixed = Unique.objects.all()
        cat = Gallery_category.objects.all()
        members = Team.objects.all()
        publish = Publications.objects.all()
        return render(request, 'home_edit.html', {'slider': slider, 'fixed': fixed, 'cnt': cnt, 'pic': pic, 'cat': cat,'members':members,'publish':publish})
    except:
        b = request.POST['identity_heading']
        c = request.POST['identity_data']
        Unique.objects.filter(id=id).update(identity_heading=b,identity_data=c);
        slider = Slider.objects.all()
        pic = Gallery.objects.all()
        cnt = Contact.objects.all()
        fixed = Unique.objects.all()
        cat = Gallery_category.objects.all()
        members = Team.objects.all()
        publish = Publications.objects.all()
        return render(request, 'home_edit.html', {'slider': slider, 'fixed': fixed, 'cnt': cnt,'pic':pic,'cat':cat,'members':members,'publish':publish})

def update_patron2(request):
    id = request.POST['id']
    try:
        a = request.POST['patron2_description']
        b = request.FILES['patron2']
        Unique.objects.filter(id=id).update(patron2_description=a, patron2=b);
    except:
        a = request.POST['patron2_description']
        Unique.objects.filter(id=id).update(patron2_description=a);
    slider = Slider.objects.all()
    pic = Gallery.objects.all()
    cnt = Contact.objects.all()
    fixed = Unique.objects.all()
    cat = Gallery_category.objects.all()
    members = Team.objects.all()
    publish = Publications.objects.all()
    return render(request, 'home_edit.html', {'slider': slider, 'fixed': fixed, 'cnt': cnt, 'pic': pic, 'cat': cat,'members':members,'publish':publish})

def update_patron1(request):
    id = request.POST['id']
    try:
        a = request.POST['patron1_description']
        b = request.FILES['patron1']
        Unique.objects.filter(id=id).update(patron1_description=a, patron1=b);
    except:
        a = request.POST['patron1_description']
        Unique.objects.filter(id=id).update(patron1_description=a);
    slider = Slider.objects.all()
    pic = Gallery.objects.all()
    cnt = Contact.objects.all()
    fixed = Unique.objects.all()
    cat = Gallery_category.objects.all()
    members = Team.objects.all()
    publish = Publications.objects.all()
    return render(request, 'home_edit.html', {'slider': slider, 'fixed': fixed, 'cnt': cnt, 'pic': pic, 'cat': cat,'members':members,'publish':publish})

def update_patron3(request):
    id = request.POST['id']
    try:
        a = request.POST['patron3_description']
        b = request.FILES['patron3']
        Unique.objects.filter(id=id).update(patron3_description=a, patron3=b);
    except:
        a = request.POST['patron3_description']
        Unique.objects.filter(id=id).update(patron3_description=a);
    slider = Slider.objects.all()
    pic = Gallery.objects.all()
    cnt = Contact.objects.all()
    fixed = Unique.objects.all()
    cat = Gallery_category.objects.all()
    members = Team.objects.all()
    publish = Publications.objects.all()
    return render(request, 'home_edit.html', {'slider': slider, 'fixed': fixed, 'cnt': cnt, 'pic': pic, 'cat': cat,'members':members,'publish':publish})
def update_mission(request):
    id = request.POST['id']
    try:
        a = request.POST['mission_data']
        b = request.FILES['mission_cover']
        Unique.objects.filter(id=id).update(mission_data=a, mission_cover=b);
    except:
        a = request.POST['mission_data']
        Unique.objects.filter(id=id).update(mission_data=a);
    slider = Slider.objects.all()
    pic = Gallery.objects.all()
    cnt = Contact.objects.all()
    fixed = Unique.objects.all()
    cat = Gallery_category.objects.all()
    members = Team.objects.all()
    publish = Publications.objects.all()
    return render(request, 'home_edit.html', {'slider': slider, 'fixed': fixed, 'cnt': cnt, 'pic': pic, 'cat': cat,'members':members,'publish':publish})

def team_update(request):
    id = request.POST['id']
    try:
        a = request.POST['member_name']
        b = request.POST['member_role']
        c = request.FILES['team_members']
        d = request.POST['member_description']
        Team.objects.filter(id=id).update(member_name=a, member_role=b,team_members=c,member_description=d);
    except:
        a = request.POST['member_name']
        b = request.POST['member_role']
        d = request.POST['member_description']
        Team.objects.filter(id=id).update(member_name=a,member_role=b,member_description=d);
    slider = Slider.objects.all()
    pic = Gallery.objects.all()
    cnt = Contact.objects.all()
    fixed = Unique.objects.all()
    cat = Gallery_category.objects.all()
    members = Team.objects.all()
    publish = Publications.objects.all()
    return render(request, 'home_edit.html',{'slider': slider, 'fixed': fixed, 'cnt': cnt, 'pic': pic, 'cat': cat, 'members': members,'publish': publish})

def publish_update(request):
    id = request.POST['id']
    try:
        a = request.POST['book_description']
        b = request.FILES['book']
        Publications.objects.filter(id=id).update(book_description=a, book=b);
    except:
        a = request.POST['book_description']
        Publications.objects.filter(id=id).update(book_description=a);
    slider = Slider.objects.all()
    pic = Gallery.objects.all()
    cnt = Contact.objects.all()
    fixed = Unique.objects.all()
    cat = Gallery_category.objects.all()
    members = Team.objects.all()
    publish = Publications.objects.all()
    return render(request, 'home_edit.html',{'slider': slider, 'fixed': fixed, 'cnt': cnt, 'pic': pic, 'cat': cat, 'members': members,'publish': publish})


def gallery_category_delete(request):
    print("hello1")
    id = request.POST['id']
    print("hello")
    print(id)
    cnt = Contact.objects.all()
    fixed = Unique.objects.all()
    slider = Slider.objects.all()
    cat = Gallery_category.objects.get(id=id)

    pic= Gallery.objects.filter(function_name = cat.function_name)
    pic.delete()
    cat.delete()
    return render(request, 'gallery_category_delete.html',{'slider': slider, 'fixed': fixed, 'cnt': cnt, 'pic': pic, 'cat': cat})

def add_gallery(request):
    cnt = Contact.objects.all()
    fixed = Unique.objects.all()
    slider = Slider.objects.all()
    a = request.FILES['image']
    b = request.POST['function_name']
    cat = Gallery_category.objects.all()
    pic = Gallery.objects.all()
    data = Gallery(image=a,function_name=b)
    data.save();
    return render(request, 'gallery_category_delete.html', {'slider': slider, 'fixed': fixed, 'cnt': cnt, 'pic': pic, 'cat': cat})