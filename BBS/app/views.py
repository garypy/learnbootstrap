# Create your views here.
from django.template import RequestContext
from django.shortcuts import render_to_response
from django.http import HttpResponse
from app import models

def index(request):
    #return render_to_response('bbs/index.html')
    bbs_list = models.BBS.objects.all() 
    return render_to_response('index.html', {'bbs_list' : bbs_list})

def page(request, bbs_id):
    bbs = models.BBS.objects.get(id=bbs_id)
    return render_to_response('page.html', {'bbs_obj' : bbs})
