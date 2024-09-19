from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from porfolio.views import InvestmentViewSet, InvestmentHistoryViewSet

router = DefaultRouter()
router.register(r'investments', InvestmentViewSet)
router.register(r'history', InvestmentHistoryViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
]
