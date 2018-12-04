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
 
 array = [1,2,3,4,5,6,7,8,9,0]
 print(array[0:2])
 print(array[-1])


 colours = [ "red", "green", "yellow", "blue" ]
 things = [ "house", "car", "tree" ]
 coloured_things = [ (x,y) for x in colours for y in things ]
 print(coloured_things)

 print([i for i in range(array.__len__()) if i % 2==0  ])
 x=2
 y=2
 z=2
 n=2
 print ([[a,b,c] for a in range(0,x+1) for b in range(0,y+1) for c in range(0,z+1) if a + b + c != n ])

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