# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import datetime

from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from django.utils import timezone

# Create your models here.

@python_2_unicode_compatible
class Question (models.Model):
  question_text = models.CharField(max_length=200)
  pub_date = models.DateTimeField('date published')
  def __str__(self):
   return self.question_text
  def was_published_recently(input):
# return boolean true if pub_date > today or yesterday
   now = timezone.now()
   return now - datetime.timedelta(days=1) <= input.pub_date <= now #seperti self dia bisa mengambil parameter pada diri sendiri


@python_2_unicode_compatible
class Choice (models.Model):
  question = models.ForeignKey(Question, on_delete=models.CASCADE )
  choice_text = models.CharField(max_length=200)
  votes = models.IntegerField(default=0)
  def __str__(self):
   return self.choice_text

@python_2_unicode_compatible
class Customer (models.Model):
 name = models.CharField(max_length=200)
 addres = models.CharField(max_length=200)
 gender = ( ('F','FEMALE'),('M','MALE'))
 sex = models.CharField(max_length=1, choices=gender)
 def __str__(self):
  return self.name

@python_2_unicode_compatible
class car (models.Model):
 type_name = models.CharField(max_length=200)
 brand_name = models.CharField(max_length=200)
 car_id = models.ForeignKey(Customer, on_delete=models.CASCADE )
 def __str__(self):
  return self.type_name

@python_2_unicode_compatible
class Transaksi (models.Model):
 customer_id = models.CharField(max_length=200)
 trx_date = models.DateTimeField('transaction date')
 trx_amount = models.DecimalField(max_digits=8, decimal_places=2)
 #year = models.CharField(max_length=200)
 #month =  models.CharField(max_length=200)
 #day =  models.CharField(max_length=200)
 #sum =  models.DecimalField(max_digits=10, decimal_places=2)
 #count =  models.IntegerField(default=0)
 def __str__(self):
  return u'%s %s %s' % (self.customer_id, self.trx_date, self.trx_amount)


class Meta:
 ordering = ('created',)


