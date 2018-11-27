

from rest_framework import serializers
from .models import Transaksi


class TransaksiSerializer(serializers.ModelSerializer):
 class Meta:
  model = Transaksi
  fields = ('id', 'customer_id', 'trx_date', 'trx_amount')

# id = serializers.IntegerField(read_only=True)
# customer_id = serializers.CharField(max_length=200)
# trx_date = serializers.DateTimeField()
# trx_amount = serializers.DecimalField(max_digits=8, decimal_places=2)

def create(self, validated_data):
 #Create and return a new `Transaksi` instance, given the validated data.
 return Transaksi.objects.create(**validated_data)

def update(self, instance, validated_data):
 #Update and return an existing `Transaksi` instance, given the validated data.
 instance.customer_id = validated_data.get('customer_id', instance.customer_id)
 instance.trx_date = validated_data.get('trx_date', instance.trx_date)
 instance. trx_amount = validated_data.get('trx_amount', instance.trx_amount)
 instance.save()
 return instance
