# myproject
Python Project

Project aplikasi polling dengan menggunakan backend mysql

====================================================================================
https://www.digitalocean.com/community/tutorials/how-to-use-web-apis-in-python-3 ==> call https
https://linuxconfig.org/how-to-parse-data-from-json-into-python 
https://www.tecmint.com/install-ntp-server-in-centos/
https://www.programcreek.com/python/example/85794/http.client.HTTPSConnection ==> sample https connection
https://www.journaldev.com/19213/python-http-client-request-get-post#getting-the-header-list-from-response ===> connect to back end
====================================================================================

Setup Django
https://pip.pypa.io/en/stable/installing/
https://ipstack.com/
================================to solve problem=====================================
 nyari di repo
  sudo yum list \*mysql\* | grep dev

   

   python manage.py createsuperuser candra/andromeda (di DIT admin/P@ssw0rd)
   
   Publick IP
 python manage.py runserver 0:8000
 
 check Sytanx
 python -m py_compile urls.py
======================================================================================
======================= enviroment Set up ============================================
python --version
python get-pip.py
Setup bash rc
add PATH --> PATH=$PATH:$HOME/.local/bin

export PATH

pip install --user pipenv
pipenv install --user requests

virtualenv env
source env/bin/activate


pip install --user virtualenv
pip install --user virtualenvwrapper
mkvirtualenv myproject
workon myproject


git clone https://github.com/django/django.git

python -m pip install --upgrade pip setuptools
python -m pip install --user django
pip install djangorestframework

django-admin startproject mysite
python manage.py startapp polls

pip install --user pymysql

And add this to your manage.py:

import pymysql
pymysql.install_as_MySQLdb()

python manage.py migrate

==========================================================================================

create class models

https://docs.djangoproject.com/en/1.11/intro/tutorial02/

python manage.py makemigrations polls
By running makemigrations, you’re telling Django that you’ve made some changes to your models (in this case, you’ve made new ones) and that you’d like the changes to be stored as a migration.

python manage.py sqlmigrate polls 0001

3 IMPORTANT STEP


    Change your models (in models.py).
    Run python manage.py makemigrations to create migrations for those changes
    Run python manage.py migrate to apply those changes to the database.

==========================================================================================
python manage.py shell

modify table without touch database

>>>>>> q = Question(question_text="What's new?", pub_date=timezone.now()) ==> Insert atau inisiasi, sama dengan q=Question() , q.question_text = "halii ??". jika suatu variable sudah di isi bisa langsung di panggil

>>> q = Question()
>>> q.question_text = 'hai haiiii ?'
>>> q.pub_date = mydate
>>> q.was_published_recently()
False

>>>>>>> q.save() ==> save data base

>>> c = Choice.objects.get(id='1') ===> filter nya dulu
>>> c.votes ==> untuk memilih kolom nya
>>> c[0].votes ===> jika Object nya banyak
0
>>> c.choice_text
u'Not much'


Creating an admin user
 python manage.py createsuperuser
 10.1.83.153:8081/admin/
 

 
{% if latest_question_list %}
    <ul>
    {% for question in latest_question_list %}
        <li><a href="/polls/{{ question.id }}/">{{ question.question_text }}</a></li>
    {% endfor %}
    </ul>
{% else %}
    <p>No polls are available.</p>
{% endif %}


{% if customer.name  %}
<ul>
<li>
{{ customer.name }} : {{ customer.addres }} : {{ customer.sex }}
</li>
</ul>
{%  for car in customer.car_set.all %}
<li>
{{ car.type_name }}
{{ car.brand_name }}
</li>

>>> customer = Customer.objects.get(pk=1)
>>> customer
<Customer: Candra>
>>>
>>> customer.car_set.all() ====> semua mobil yang dimiliki candra
<QuerySet [<car: hatch back>, <car: SUV>]>

- descending
===============================================================================================================================
	try:
        question = Question.objects.get(pk=question_id)
    except Question.DoesNotExist:
        raise Http404("Question does not exist")
=========================================== dapat diganti menjadi  ===== question = get_object_or_404(Question, pk=question_id)

Recently

 now = timezone.now()
   return now - datetime.timedelta(days=1) <= input.pub_date <= now

===== SQL mencari yang unix===========================================
select count(distinct customer_id) from polls_transaksi ;
===== SQL mencari yang id nya kembar untuk di edit====================
SELECT * FROM polls_transaksi WHERE customer_id IN (    SELECT customer_id    FROM polls_transaksi     GROUP BY customer_id    HAVING COUNT(*) > 1)

========================================== mencari jumlah yang kembar ========================
 SELECT customer_id, count(*) FROM polls_transaksi group by customer_id having count(*) > 1;
 ================================= post GRESQL ====================================================
 select * from (
  SELECT id,
  ROW_NUMBER() OVER(PARTITION BY merchant_Id, url ORDER BY id asc) AS Row
  FROM Photos
) dups
where 
dups.Row > 1

keytool -v -importkeystore -srckeystore alice.p12 -srcstoretype PKCS12 -destkeystore truststore.jks -deststoretype JKS
============================================================ extension ==========================================
pip install django-extensions
mkdir scripts
touch scripts/__init__.py

 python ../manage.py runscript test_dict
=================================================================================================================
from polls.models import Transaksi
from polls.models import Customer , car
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from polls.serializers import TransaksiSerializer
from django.utils.six import BytesIO
import datetime

from django.db.models import Sum, Count
from django.db.models.functions import TruncMonth
from django.db.models.functions import TruncDay
from django.db.models.functions import TruncYear
from django.db import connection

>>> print(t.query)

t = Transaksi.objects.filter(trx_date__year=2017)

t = Transaksi.objects.get(pk=1)
serializer = TransaksiSerializer(t, many=True)
serializer.data
content = JSONRenderer().render(serializer.data[1])
content
serializer = TransaksiSerializer(Transaksi.objects.filter(trx_date__year=2017), many=True)
serializer.data

serializer = TransaksiSerializer(Transaksi.objects.filter(trx_date__month=06), many=True)

stream = BytesIO(content)
data = JSONParser().parse(stream)
serializer = TransaksiSerializer(data=data)
serializer.is_valid()
serializer.validated_data
 s = TransaksiSerializer(t)
 
 
 body_unicode = request.body.decode('utf-8')
body = json.loads(body_unicode)
content = body['content']

body_unicode = request.body.decode('utf-8')
body_data = json.loads(body_unicode)

7-7

SELECT * , EXTRACT(MONTH FROM `polls_transaksi`.`trx_date`) as month from polls_transaksi WHERE EXTRACT(MONTH FROM `polls_transaksi`.`trx_date`) = 6 

SELECT count(distinct(customer_id)) FROM polls_transaksi WHERE EXTRACT(MONTH FROM `polls_transaksi`.`trx_date`) = 6 

SELECT count(distinct(customer_id)) FROM polls_transaksi WHERE EXTRACT(MONTH FROM `polls_transaksi`.`trx_date`) = 6 
SELECT * FROM polls_transaksi WHERE EXTRACT(HOUR FROM `polls_transaksi`.`trx_date`) < 7
SELECT count(distinct(customer_id)) FROM polls_transaksi where trx_date between  "2017-09-26 13:43" and "2017-11-27 13:43"

SELECT count(distinct(customer_id)) FROM polls_transaksi where EXTRACT(MONTH FROM `polls_transaksi`.`trx_date`) = 10

SELECT CAST(DATE_FORMAT(`polls_transaksi`.`trx_date`, '%Y-%m-%d 00:00:00') AS DATETIME) AS `day`, SUM(`polls_transaksi`.`trx_amount`) AS `sum` FROM `polls_transaksi` WHERE `polls_transaksi`.`trx_date` BETWEEN "2017-08-26 13:43:00" AND "2017-11-26 13:43:00" GROUP BY CAST(DATE_FORMAT(`polls_transaksi`.`trx_date`, '%Y-%m-%d 00:00:00') AS DATETIME), `polls_transaksi`.`trx_date` ORDER BY `polls_transaksi`.`trx_date` ASC

==========================================================================================================================================================

s = str(t[1].trx_amount)

t = Transaksi.objects.filter(trx_date__month=6).aggregate(Sum('trx_amount'))
t =  Transaksi.objects.filter(trx_date__range=("2017-09-26 13:43","2017-11-26 13:43")).aggregate(Sum('trx_amount'))

-==========================================================================================================================================
from django.db.models.functions import TruncMonth
Sales.objects
    .annotate(month=TruncMonth('timestamp'))  # Truncate to month and add to select list
    .values('month')                          # Group By month
    .annotate(c=Count('id'))                  # Select the count of the grouping
    .values('month', 'c') 
	
===========================================================================================================================================	

t = Transaksi.objects.filter(trx_date__range=("2017-09-26 13:43","2017-11-26 13:43")).annotate(month=TruncMonth('trx_date')).values('month').annotate(sum=Sum('trx_amount')).values('month', 'sum')



t = Transaksi.objects.filter(trx_date__range=("2017-08-26 13:43","2017-11-26 13:43")).annotate(day=TruncDay('trx_date')).values('day').annotate(sum=Sum('trx_amount')).values('day', 'sum')
print(t.query)


t = Transaksi.objects.filter(trx_date__range=("2017-09-26 13:43","2017-11-26 13:43")).annotate(year=TruncYear('trx_date')).values('year').annotate(sum=Sum('trx_amount')).values('year', 'sum')

t[1]['month'].strftime('%Y-%m-%d')

finaldict[t[1]['month'].strftime('%Y-%m-%d')]=str(t[1]['sum'])
finaldict[t[x]['month'].strftime('%Y-%m-%d')]=str(t[x]['sum'])

time.strftime('%Y-%m-%dT%H:%M')

dict start from zero
exec("for x in range(0,t.__len__()): finaldict[t[x]['month'].strftime('%Y-%m-%d')]=str(t[x]['sum'])")

{'sum': Decimal('2851394.00'), 'day': datetime.datetime(2017, 10, 20, 0, 0)}


==============================
https://pythonspot.com/json-encoding-and-decoding-with-python/

================================

distinct=True

====== month ====
t = Transaksi.objects.filter(trx_date__range=("2017-09-26 13:43","2017-11-26 13:43")).annotate(month=TruncMonth('trx_date')).values('month').annotate(count=Count('customer_id',distinct=True)).values('month', 'count')


====== year ====
t = Transaksi.objects.filter(trx_date__range=("2017-09-26 13:43","2017-11-26 13:43")).annotate(year=TruncYear('trx_date')).values('month').annotate(count=Count('customer_id',distinct=True)).values('year', 'count')


====== daily ====
t = Transaksi.objects.filter(trx_date__range=("2017-09-26 13:43","2017-11-26 13:43")).annotate(day=TruncDay('trx_date')).values('day').annotate(count=Count('customer_id',distinct=True)).values('day', 'count')

==============================

exec("for x in range(0,t.__len__()): finaldict[t[x]['month'].strftime('%Y-%m-%d')]=str(t[x]['count']) print(x)")
exec("for i in range(transaksis.__len__()):cache.set(transaksis[i].customer_id, transaksis[i], timeout=CACHE_TTL)")

curl 'http://10.1.83.153:9080/git/notifyCommit?url=ssh://git@10.1.83.227:10022/playground.git'

a = ['1','2','3']
a += ['b']
a = ['1','2','3','b']

==================================== Redis =========================================================
https://code.tutsplus.com/id/tutorials/how-to-cache-using-redis-in-django-applications--cms-30178
https://django-redis-cache.readthedocs.io/en/latest/api.html
sudo service redis start
====================================================================================================
https://niwinz.github.io/django-redis/latest/#_get_ttl_time_to_live_from_key == redis
=====================================================================================================

free -m | awk '/:/ {print $2;exit}'

substring ambil ke

line.split("=")[1]

========================== object ================= class ==============

class Complex:
   def __init__(self, realpart, imagpart):  #===== default constructor(java) , self == wajib,(menandakan constructor), realpart == parameter, imagpart == parameter=============
       self.r = realpart
       self.i = imagpart
	   
	   
>>> x = Complex(3.0, -4.5)
>>> x.r, x.i
(3.0, -4.5)
==================================================================
ctrl+shift+p === visual studio to selece intepreter







