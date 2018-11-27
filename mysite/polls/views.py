
# -*- coding: utf-8 -*-
#!/usr/bin/python
"candra"
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
from rest_framework.decorators import api_view
import http.client

@csrf_exempt
@api_view(['POST'])
def login(request):
  json_data = json.loads(request.body)
  pasword = json_data['password']
  username = json_data['username']
  conn = http.client.HTTPSConnection("appapisit01.dev.corp.btpn.co.id:19502")

  payload = '{\n  \"id\": 0,\n  \"password\": \"'+str(pasword)+'\",\n  \"username\": \"'+str(username)+'\"\n}'

  headers = {
    'cookie': "078a3db85f58775f83e1b825b3327bca=de28a0e045bb3ff1f2debdc71c209497; eff4294aac91f7875a5e14dd91a79dd0=1cddf6178199e708cf184eca27a02232",
    'content-type': "application/json",
    'btpn-apikey': "c50dda12-9fd4-4aa2-9311-2882e7122e0b"
    }

  conn.request("POST", "/base/login", payload, headers)
  res = conn.getresponse()
  JWT = res.getheader("X-BTPN-JWT")
  #JWT = "dasdsadsad"
  
  data = res.read()
  

  #print(data.decode("utf-8"))
  customrespons = HttpResponse(data.decode("utf-8"))
  customrespons.__setitem__('JWT',JWT)
  customrespons.__setitem__('Content-Type','application/json')
  return customrespons


@csrf_exempt
def transaksi_list(request):
    #"""
    #List all code Transaksi, or create a new snippet.
    #"""
 if request.method == 'GET':
  transaksis = Transaksi.objects.all()
  serializer = TransaksiSerializer(transaksis, many=True)
  return JsonResponse(serializer.data, safe=False)
 elif request.method == 'POST':
  data = JSONParser().parse(request)
  serializer = TransaksiSerializer(data=data)
 if serializer.is_valid():
    serializer.save()
    return JsonResponse(serializer.data, status=201)
 return JsonResponse(serializer.errors, status=400)
  
@csrf_exempt
def query(request):
 if request.method == 'POST':
  #output = { "coba" : "coba" }
  #body_unicode = request.body.decode('utf-8')
  #body = json.loads(body_unicode)
  json_data = json.loads(request.body)
  startDate = json_data['startDate']
  endDate = json_data['endDate']
  agregationLevel = json_data['agregationLevel']
  #renderer_classes = (JSONRenderer, )
  media_type = 'application/json'
  
  if agregationLevel.lower() == 'monthly':
   json_string = (sumMonth(startDate,endDate))
  elif agregationLevel.lower() == 'daily':
   json_string = (sumDay(startDate,endDate))
  elif agregationLevel.lower() == 'yearly':
   json_string = (sumYear(startDate,endDate))
  else :
   return HttpResponse(status=404)  

  output = { "startDate" : startDate,
             "endDate"   : endDate,
             "agregationLevel" : agregationLevel,
             #"query" :  json.dumps(json_string).replace('\\','')
	     #"query" : str(json.dumps(json_string)).replace("\\","")
	     "query" : json_string	 
           }

  return JsonResponse(output, safe=False)

 return HttpResponse(status=400)
  
  
@csrf_exempt
def customers(request):
 if request.method == 'POST':
  #output = { "coba" : "coba" }
  #body_unicode = request.body.decode('utf-8')
  #body = json.loads(body_unicode)
  json_data = json.loads(request.body)
  startDate = json_data['startDate']
  endDate = json_data['endDate']
  agregationLevel = json_data['agregationLevel']
  #renderer_classes = (JSONRenderer, )
  media_type = 'application/json'

  if agregationLevel.lower() == 'monthly':
   json_string = (sumcustomerMonth(startDate,endDate))
  elif agregationLevel.lower() == 'daily':
   json_string = (sumcustomerDay(startDate,endDate))
  elif agregationLevel.lower() == 'yearly':
   json_string = (sumcustomerYear(startDate,endDate))
  else:
   return HttpResponse(status=404)  

  output = { "startDate" : startDate,
             "endDate"   : endDate,
             "agregationLevel" : agregationLevel,
             "query" :  json_string
           }

  return JsonResponse(output)

 return HttpResponse(status=400)
 
@csrf_exempt
def transaksi_detail(request, pk):
    #"""
    #Retrieve, update or delete a code snippet.
    #"""
 transaksi = Transaksi.objects.filter(customer_id=pk)
 if transaksi:
  if request.method == 'GET':
   #data nya bisa bnyak bisa satu. kalau pakai first tidak bisa di iterable.
   serializer = TransaksiSerializer(transaksi, many=True )
   return JsonResponse(serializer.data, safe=False)
  elif request.method == 'PUT':
  # data harus satu maka perlu pakai first.
  # trx = Transaksi.objects.filter(customer_id=pk).first() 
   trx = Transaksi.objects.filter(customer_id=pk)
   data = JSONParser().parse(request)
   #atau ambil saja data yang pertama trx[1]
   serializer = TransaksiSerializer(trx[1], data=data)
   if serializer.is_valid():
      serializer.save()
      return JsonResponse(serializer.data)
   return JsonResponse(serializer.errors, status=400)
  elif request.method == 'DELETE':
   transaksi.delete()
   return HttpResponse(status=204)
 return HttpResponse(status=404)



# Create your views here.
def index(request):
        latest_question_list = Question.objects.order_by('-pub_date')[:5]
        list_customer = Customer.objects.all()
        template = loader.get_template('polls/index.html')
        context = {
           'latest_question_list' : latest_question_list,
           'list_customer': list_customer,
        }        
        return HttpResponse(template.render(context, request))

        #output = ','.join([q.question_text for q in latest_question_list])
	#return HttpResponse("Hello, worl. You're at the polls index.\n",output)




def detail (request, question_id):
   try:
     question = Question.objects.get(pk=question_id)
   except Question.DoesNotExist:
     raise Http404("Question does not exist")
   return render(request, 'polls/detail.html',{'question': question})
 #return HttpResponse("youre looking at question %s." % question_id)

def results(request, question_id):
 try:
  question = Question.objects.get(pk=question_id)
 #fitur ini hanya, berlaku untuk get. yang hanya boleh mendapatkan satu record.
 except Question.DoesNotExist:
  raise Http404("Question does not Exist")
 return render(request, 'polls/result.html',{'question': question})
 #response ="you are looking at the result of question %s. "
 #return HttpResponse(response % question_id)

@csrf_exempt
def swagger(request):
 return render(request,'polls/bigdata.json')
 
@csrf_exempt
def readfile(request, id):
  file_location=r"C:\Users\17053598\sample_file_output\data.json"
  with open(file_location,'r') as data:
   jsondata = json.loads(data.readline())
  
  detail = []
  #print(jsondata)
  #jsondata['nama_object_array_diJSON_ny']
  for dt in jsondata:
    if dt['customer_id'] == str(id):
     print(dt['customer_id'])
     detail.append(dt)
    
  if detail:
    print(detail)
    return JsonResponse(detail, safe=False)
  return HttpResponse(status=404)
  #print(json.dumps(jsondata))
  #return HttpResponse(json.dumps(jsondata)) 
  #sama
  

 
 
@csrf_exempt
def peformance(request):
        amount_incoming_by_day = Transaksi.objects.filter(trx_date__range=("2017-08-26 13:43","2017-11-26 13:43")).annotate(day=TruncDay('trx_date')).order_by('day').values('day').annotate(sum=Sum('trx_amount')).values('day', 'sum')
		
        list_customer_by_day = Transaksi.objects.filter(trx_date__range=("2017-08-26 13:43","2017-11-26 13:43")).annotate(day=TruncDay('trx_date')).values('day').annotate(count=Count('customer_id',distinct=True)).values('day', 'count')
        template = loader.get_template('polls/performance.html')
        context = {
           'amounts' : amount_incoming_by_day,
           'customers': list_customer_by_day,
        }        
        return HttpResponse(template.render(context, request))

def vote(request, question_id):
 question = get_object_or_404(Question, pk=question_id)
 try:
  selected_choice = question.choice_set.get(pk=request.POST['choice'])
  print(request.POST['choice'], end='')
  #sys.stdout.flush()
 except (KeyError, Choice.DoesNotExist):
  # Redisplay the question voting form.
  return render(request, 'polls/detail.html', {
      'question': question,
      'error_message': "You didn't select a choice.",
       })
 else:
   selected_choice.votes += 1
   selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        #return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))
   return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))
 #return HttpResponse("you are voting on question %s." % question_id)

def customer(request, idc):
 try:
   customer = Customer.objects.get(pk=idc)
 except Customer.DoesNotExist: 
   raise Http404("Customer does not exist")
 return render(request,'polls/detail.html',{'customer': customer})

@csrf_exempt
def trx(request, num_of_record):
 response = "insert data sukses dengan %s. record"
#now = timezone.now() 
#now = datetime.timedelta(days=30)
 output = ""
 for i in range (1,int(num_of_record)):
  amount = random.randint(1000,1000000)
  customerid = str(random.randint(1,10000))
  randomdate = str(randomDate("2017-01-01","2018-01-01" ))
  trxdate = str(randomDatetime(randomdate+" 07:00", randomdate+" 19:01"))
  output = output+" "+trxdate+" "+str(amount)+" "+customerid+"\n"
  t = Transaksi(customer_id=customerid , trx_date=trxdate, trx_amount = amount)
  t.save()
 response = output+response
 return HttpResponse(response % num_of_record)

def strTimeProp(start, end, format ):
#Get a time at a proportion of a range of two formatted times.
#start and end should be strings specifying times formated in the
#given format (strftime-style), giving an interval [start, end].
#prop(random) specifies how a proportion of the interval to be taken after
#start.  The returned time will be in the specified format.
#

 stime = time.mktime(time.strptime(start, format))
 etime = time.mktime(time.strptime(end, format))

 ptime = stime + random.random() * (etime - stime)

 return time.strftime(format, time.localtime(ptime))

def randomDatetime(start, end ):
 return strTimeProp(start, end, '%Y-%m-%d %H:%M' )

def randomDate(start, end ):
 return strTimeProp(start, end , '%Y-%m-%d')

def sumMonth(startdate, enddate):
 mdict = Transaksi.objects.filter(trx_date__range=(startdate,enddate)).annotate(month=TruncMonth('trx_date')).order_by('month').values('month').annotate(sum=Sum('trx_amount')).values('month', 'sum')
 #finaldict = OrderedDict()
 dictlist = []
 finaldict = {}
 for x in range(0,mdict.__len__()):
  finaldict = {}
  finaldict[mdict[x]['month'].strftime('%Y-%m')]=str(mdict[x]['sum']) 
  #output= '{ '+'"'+str(mdict[x]['month'].strftime('%Y-%m') )+'"'+':'+'"'+str(finaldict[mdict[x]['month'].strftime('%Y-%m')])+'"'+' }'
  dictlist.append(finaldict.copy())
 return dictlist
 #return json.dumps(finaldict.items()).replace("[[","{").replace("[","{").replace("]]","}").replace("]","}").replace("\\","")

def sumYear(startdate, enddate):
 mdict = Transaksi.objects.filter(trx_date__range=(startdate,enddate)).annotate(year=TruncYear('trx_date')).order_by('year').values('year').annotate(sum=Sum('trx_amount')).values('year', 'sum')
 finaldict = {}
 dictlist = []
 for x in range(0,mdict.__len__()):
  finaldict = {}
  finaldict[mdict[x]['year'].strftime('%Y')]=str(mdict[x]['sum'])
  #output= '{ '+'"'+str(mdict[x]['year'].strftime('%Y') )+'"'+':'+'"'+str(finaldict[mdict[x]['year'].strftime('%Y')])+'"'+' }'
  dictlist.append(finaldict.copy())
 return dictlist

def sumDay(startdate, enddate):
 mdict = Transaksi.objects.filter(trx_date__range=(startdate,enddate)).annotate(day=TruncDay('trx_date')).order_by('day').values('day').annotate(sum=Sum('trx_amount')).values('day', 'sum')
 finaldict = {}
 dictlist = []
 for x in range(0,mdict.__len__()):
  finaldict = {}
  finaldict[mdict[x]['day'].strftime('%Y-%m-%d')]=str(mdict[x]['sum'])
  #output= '{ '+"'"+str(mdict[x]['day'].strftime('%Y-%m-%d') )+"'"+':'+str(finaldict[mdict[x]['day'].strftime('%Y-%m-%d')])+' }'
  dictlist.append(finaldict.copy())
 return dictlist

def sumcustomerMonth(startDate,endDate):
 mdict = Transaksi.objects.filter(trx_date__range=(startDate,endDate)).annotate(month=TruncMonth('trx_date')).order_by('month').values('month').annotate(count=Count('customer_id',distinct=True)).values('month', 'count')
 finaldict = {}
 dictlist = []
 for x in range(mdict.__len__()):
  finaldict = {}
  finaldict[mdict[x]['month'].strftime('%Y-%m')]=str(mdict[x]['count'])
  #output= '{ '+'"'+str(mdict[x]['month'].strftime('%Y-%m') )+'"'+':'+'"'+str(finaldict[mdict[x]['month'].strftime('%Y-%m')])+'"'+' }'
  dictlist.append(finaldict.copy())
 return dictlist

def sumcustomerYear(startDate,endDate):
 mdict = Transaksi.objects.filter(trx_date__range=(startDate,endDate)).annotate(year=TruncYear('trx_date')).order_by('year').values('year').annotate(count=Count('customer_id',distinct=True)).values('year', 'count')
 finaldict = {}
 dictlist = []
 for x in range(0,mdict.__len__()):
  finaldict = {}
  finaldict[mdict[x]['year'].strftime('%Y')]=str(mdict[x]['count'])
  #output= '{ '+'"'+str(mdict[x]['year'].strftime('%Y') )+'"'+':'+'"'+str(finaldict[mdict[x]['year'].strftime('%Y')])+'"'+' }'
  dictlist.append(finaldict.copy())
 return dictlist

def sumcustomerDay(startDate,endDate):
 mdict = Transaksi.objects.filter(trx_date__range=(startDate,endDate)).annotate(day=TruncDay('trx_date')).values('day').annotate(count=Count('customer_id',distinct=True)).values('day', 'count')
 finaldict = {}
 dictlist = []
 for x in range(0,mdict.__len__()):
  finaldict = {}
  finaldict[mdict[x]['day'].strftime('%Y-%m-%d')]=str(mdict[x]['count'])
  #output= '{ '+'"'+str(mdict[x]['day'].strftime('%Y-%m-%d') )+'"'+':'+'"'+str(finaldict[mdict[x]['day'].strftime('%Y-%m-%d')])+'"'+' }'
  dictlist.append(finaldict.copy())
 return dictlist


