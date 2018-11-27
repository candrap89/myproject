from django.shortcuts import render
#from __future__ import print_function
from django.http import HttpResponse
from django.template import loader
from django.http import Http404
from django.shortcuts import render
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.utils import timezone
import datetime
from .models import Question
from .models import Customer
from .models import Choice
from .models import Transaksi
import sys
import time
import random
import json
import time
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from .serializers import TransaksiSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from django.db.models import Sum, Count
from django.db.models.functions import TruncMonth
from django.db.models.functions import TruncDay
from django.db.models.functions import TruncYear
from collections import OrderedDict 
from django.conf import settings
from datetime import datetime
from django.core.cache.backends.base import DEFAULT_TIMEOUT
CACHE_TTL = getattr(settings, 'CACHE_TTL', DEFAULT_TIMEOUT)
from django.core.cache import cache
from rest_framework.decorators import api_view

@csrf_exempt
@api_view(['GET'])
def push(request):
 transaksis = Transaksi.objects.all()
 tm = datetime.utcnow().strftime('%Y-%m-%dT%H:%M:%S.%f')[:-3]
 for i in range(transaksis.__len__()):
  cache.set(transaksis[i].customer_id+"_"+str(tm), transaksis[i], timeout=None)
 
 return HttpResponse(status=200)
 
@csrf_exempt
@api_view(['GET'])
def pull(request,id):
  t =[]
  final = []
  t = cache.keys(str(id)+"_*")
  print(t)
  if t:
   for i in range(len(t)):
    record = cache.get(str(t[i]))
    #print(record)
    #content = ""
    serializer=TransaksiSerializer(record)
    print(serializer.data)
    content = json.dumps(serializer.data).replace('\\','')
    final.append(content)
   print (json.dumps(final).replace('\\',''))
   return HttpResponse(json.dumps(final).replace('\\',''), content_type='application/json')
  else:
    datatransaksi = Transaksi.objects.filter(customer_id__startswith=str(id))
    if datatransaksi:
     for i in range(len(datatransaksi)):
      
      cache.set(datatransaksi[i].customer_id+"_"+datetime.utcnow().strftime('%Y-%m-%dT%H:%M:%S.%f')[:-3], datatransaksi[i], timeout=None)
      
     serializer = TransaksiSerializer(datatransaksi, many=True)
     content = json.dumps(serializer.data).replace('\\','')
     return HttpResponse(content, content_type='application/json')
    return HttpResponse(status=404)

 
@csrf_exempt
def clear(request):
 return HttpResponse(status=200)