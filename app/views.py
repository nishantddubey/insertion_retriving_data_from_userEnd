from django.shortcuts import render
from app.models import *
# Create your views here.

def create_topic(request):
    if request.method == 'POST':
        tn = request.POST['tn']
        
        TO = TOPIC.objects.get_or_create(topic_name=tn)[0]
        TO.save()
        
        QLTO = TOPIC.objects.all()
        d = {"topic":QLTO}
        return render (request,'display_topic.html',d)
    
    return render(request,'create_topic.html')

    

def create_webpage(request):
        
    QLTO = TOPIC.objects.all()
    d = {"topic":QLTO}  
    if request.method=='POST':
        tn = request.POST.get('tn')
        nm = request.POST.get('nm')
        ur = request.POST.get('ur')
        em = request.POST.get('em')
        
        TO = TOPIC.objects.get(topic_name=tn)
        WO = WEBPAGE.objects.get_or_create(topic_name = TO,name = nm,url=ur,email=em)[0]
        WO.save()
        
        QLWO = WEBPAGE.objects.all()
        d1 = {'webpages':QLWO}
        
        return render(request,'display_webpages.html',d1)
        
    return render(request,'create_webpage.html',d)


def select_multiple(request):
    QLTO = TOPIC.objects.all()
    d = {"topic":QLTO}  
    if request.method=='POST':
        topiclist = request.POST.getlist('tn')
        QLWO = WEBPAGE.objects.none()
        
        for topic_name in topiclist:
            QLWO =QLWO| WEBPAGE.objects.filter(topic_name=topic_name)
        
        d1 = {'webpages': QLWO}
        return render(request,'display_webpages.html',d1)
        
    
    return render(request,'select_multiple.html',d)


def insert_accessrecord(request):
    QLWO = WEBPAGE.objects.all()
    d = {'webpages':QLWO}
    if request.method=='POST':
        nm = request.POST['nm']
        date = request.POST['date']
        auth = request.POST['auth']
        
        p = WEBPAGE.objects.get(pk=nm)
        
        AO = Accessrecord.objects.get_or_create(name=p,date=date,author=auth)[0]
        AO.save()
        
        QLAO = Accessrecord.objects.all()
        d1 = {'accessrecord':QLAO}
        return render(request,'display_accessrecord.html',d1)
    return render(request,'insert_accessrecord.html',d)
