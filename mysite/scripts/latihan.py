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
 dict_of_class = {}
 for i in range(1,10):
  x= Complex(i,i+1)
  dict_of_class[x.y]=x.r

 print(json.dumps(dict_of_class))
 z = 0
 for x,y in dict_of_class.items():
  z += 1   
  #print("key"+i+": "+str(x))
  #print("value"+i+": "+str(y))
  print("key {} : {}".format(z,x))
  print("Value {} : {}".format(z,y))

 c = Coba()
 print(c.get_definition("book"))




class Coba:
  x = 0
  y = 0
  dicw = {"book":"sheet and paper","rain":"water"}

  def asign_x_y(self):
    return u'%s %s' % (self.x, self.y)

  def get_definition(self, word):
   return self.dicw[word]
  

class Complex:
 r = 0
 y = 0 

 def __init__(self, realpart, imagpart):  #===== default constructor(java) , self == wajib,(menandakan constructor), realpart == parameter, imagpart == parameter=============
  self.r = realpart
  self.y = imagpart

 def assign(self):
  return self.r