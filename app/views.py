from django.shortcuts import render
from app.models import *

# Create your views here.


def insert(request):
     if request.method=='POST':
          tn=request.POST['tn']
          TO=Topic.objects.get_or_create(topic_name=tn)[0]

          TO.save()
          QLTO=Topic.objects.all()
          d={'topics':QLTO}
          return render(request,'display_topic.html',d)
     return render(request,'insert.html')