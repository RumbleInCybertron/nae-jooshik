from rest_framework import serializers
from .models import Investment, InvestmentHistory

class InvestmentSerializer(serializers.ModelSerializer):
  class Meta:
    model = Investment
    fields = '__all__'
    
class InvestmentHistorySerializer(serializers.ModelSerializer):
  class Meta:
    model = InvestmentHistory
    fields = '__all__'