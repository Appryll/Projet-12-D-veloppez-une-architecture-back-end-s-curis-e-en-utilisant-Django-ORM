from rest_framework import routers
from . import views
from django.urls import path, include

router=routers.DefaultRouter()
router.register('client', viewset=views.ClientList)
router.register('sales', viewset=views.SalesList)
router.register('support', viewset=views.SupportList)

urlpatterns = [
    path('', include(router.urls)),
]