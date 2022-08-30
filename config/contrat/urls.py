from rest_framework import routers
from . import views
from django.urls import path, include

router=routers.DefaultRouter()
router.register('contrat', viewset=views.ContratList, basename='contrat')

urlpatterns = [
    path('', include(router.urls)),
]
