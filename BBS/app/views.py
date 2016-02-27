# Create your views here.
from django.template import RequestContext
from django.shortcuts import render_to_response
from django.http import HttpResponse
from app import models
import datetime

def index(request):
    #return render_to_response('bbs/index.html')
    bbs_list = models.BBS.objects.all() 
    return render_to_response('index.html', {'bbs_list' : bbs_list})

def page(request, bbs_id):
    if 'cmt' in request.POST and request.POST['cmt']:
        msg = request.POST['cmt']
        #print "msg: %s" % msg
        userid = request.POST.get("userid", "")
        #print "user id: %s" % userid
        id = request.POST.get("id", "")
        #print "id: %s" % id
        now = datetime.datetime.now()#.strftime("%Y-%m-%d %H:%I:%S")
        #print "time: %s" % now
        user = models.BBS_user.objects.get(id=userid)
        comment = models.Comment(comment=msg, bbs_user=user, bbs_id=id, created_at=now)
        comment.save()
        #print "Insert sus"
    #else:
    bbs = models.BBS.objects.get(id=bbs_id)
    comments = models.Comment.objects.filter(bbs_id=bbs_id)
    return render_to_response('page.html', {'bbs_obj' : bbs, 'comments' : comments})
