# -*- coding: utf-8 -*-
#!/usr/bin/python

from polls.models import Transaksi
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from polls.serializers import TransaksiSerializer
from django.utils.six import BytesIO
import datetime
import json
from django.db.models import Sum, Count
from django.db.models.functions import TruncMonth
from django.db.models.functions import TruncDay
from django.db.models.functions import TruncYear



def run():
 mdict = Transaksi.objects.filter(trx_date__range=("2017-09-26 13:43","2017-11-26 13:43")).annotate(month=TruncMonth('trx_date')).values('month').annotate(count=Count('customer_id',distinct=True)).values('month', 'count')
 print("ok")
 
 #temp = {}
 dictlist = []
 finaldict = {} 
 
 for x in range(0,mdict.__len__()):
  finaldict = {}
  finaldict[mdict[x]['month'].strftime('%Y-%m')]=str(mdict[x]['count'])
  #output= '{ '+'"'+str(mdict[x]['month'].strftime('%Y-%m') )+'"'+':'+'"'+str(finaldict[mdict[x]['month'].strftime('%Y-%m')])+'"'+' }'
  dictlist.append(finaldict.copy())

 #for key, value in finaldict.items():
 # temp[key]=value
 # dictlist.append(#temp)
 
 jsonarray = json.dumps(dictlist)
 #jsonarray = dictlist 

 print(jsonarray)
 transaksis = Transaksi.objects.filter(customer_id=2542)
 serializer = TransaksiSerializer(transaksis, many=True)
 serializer.data
 #content = JSONRenderer().render(serializer.data[1])
 #content = JSONRenderer().render(serializer.data)
 content = json.dumps(serializer.data)
 print (transaksis.__len__())
 print (content)
 

