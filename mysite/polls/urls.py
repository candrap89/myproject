from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.urls import include


from . import views
from . import cache

app_name = 'polls'



urlpatterns = [
#debug toolbar


path('push/', cache.push ),
path('pull/<int:id>/cache', cache.pull ),
path('clear/', cache.clear ),
# ex: /polls/
path('', views.index, name='index'),
# ex: /polls/5/,
path('<int:question_id>/', views.detail, name='detail'),
# ex: /polls/5/results/
path('<int:question_id>/results/', views.results, name='results'),
# ex: /polls/5/vote/
path('<int:question_id>/vote/', views.vote, name='vote'),
# ex: /polls/5/customer/
path('<int:idc>/customer/', views.customer, name='customer'),
# generate random data to insert to DB
path('<int:num_of_record>/trx/', views.trx, name='trx'),

#get all list transaksi
path('transaksi/', views.transaksi_list),
#update transaksi
path('<int:pk>/transaksi/', views.transaksi_detail),
path('amount/', views.query ),
path('customers/', views.customers ),
path('swagger/', views.swagger),
path('peformance/',views.peformance),
path('readfile/<int:id>', views.readfile, name='id'),
path('loginservice/', views.login)
]
