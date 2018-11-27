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
  mdict = Transaksi.objects.filter(trx_date__range=("2017-09-26 13:43","2018-11-26 13:43"))
  serializer = TransaksiSerializer(mdict, many=True)
  serializer.data
  content = json.dumps(serializer.data)
  f = open(r"C:\Users\17053598\sample_file_output\data.json","w")
  f.write(content)
  print("write File Done!")
  x= Complex(4,5)
  print(x.r)
  print(x.y)
  # bisa juga seperti ini
  w = Complex(10,50)
  print(w.assign())
  
  cb = Coba()
  cb.x = 4
  cb.y =5
  print(cb.asign_x_y())


class Coba:
  x = 0
  y = 0

  def asign_x_y(self):
    return u'%s %s' % (self.x, self.y)
  

class Complex:
 r = 0
 y = 0 

 def __init__(self, realpart, imagpart):  #===== default constructor(java) , self == wajib,(menandakan constructor), realpart == parameter, imagpart == parameter=============
  self.r = realpart
  self.y = imagpart

 def assign(self):
  return self.r

class Point(object):
 def __new__(cls,*args,**kwargs):
  print("From new")
  print(cls)
  print(args)
  print(kwargs)

  # create our object and return it
  obj = super().__new__(cls)
  return obj

 def __init__(self,x = 0,y = 0):
  print("From init")
  self.x = x
  self.y = y

class SqPoint(Point):
 MAX_Inst = 4
 Inst_created = 0

def __new__(cls,*args,**kwargs):
  if (cls.Inst_created >= cls.MAX_Inst):
    raise ValueError("Cannot create more objects")
  cls.Inst_created += 1
  return super().__new__(cls)
#return (sampple melimitasi jumlah object yang bisa di create)
#>>> p1 = SqPoint(0,0)
#>>> p2 = SqPoint(1,0)
#>>> p3 = SqPoint(1,1)
#>>> p4 = SqPoint(0,1)
#>>> 
#>>> p5 = SqPoint(2,2)
#Traceback (most recent call last):
#...
#ValueError: Cannot create more objects
  
