from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from app.models import *
def insert_topic(request):
    tn=input('enter the topic_name : ')
    to=Topic.objects.get_or_create(topic_name=tn)[0]
    to.save()
    return HttpResponse('Topic_name is inserted')
def insert_web(request):
    tn=input('enter the topic_name : ')
    n=input('enter the name: ')
    url=input('enter the url: ')
    to=Topic.objects.get_or_create(topic_name=tn)[0]
    wo=Webpage.objects.get_or_create(topic_name=to,name=n,url=url)[0]
    wo.save()
    return HttpResponse('Webpage is data is inserted')
def insert_Access(request):
    tn=input('enter the topic_name : ')
    n=input('enter the name: ')
    url=input('enter the url: ')
    a=input('enter author name: ')
    d=input('enter the date: ')
    to=Topic.objects.get_or_create(topic_name='Cricket')[0]
    wo=Webpage.objects.get_or_create(topic_name=to,name=n,url=url)[0]
    ao=AccessRecord.objects.get_or_create(name=wo,author=a,date=d)[0]
    ao.save()
    return HttpResponse('AccessRecord  data is inserted')