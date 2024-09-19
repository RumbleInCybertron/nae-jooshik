from rest_framework import viewsets
from .models import Investment, InvestmentHistory
from .serializers import InvestmentSerializer, InvestmentHistorySerializer

class InvestmentViewSet(viewsets.ModelViewSet):
  queryset = Investment.objects.all()
  serializer_class = InvestmentSerializer
  
class InvestmentHistoryViewSet(viewsets.ModelViewSet):
  queryset = InvestmentHistory.objects.all()
  serializer_class = InvestmentHistorySerializer