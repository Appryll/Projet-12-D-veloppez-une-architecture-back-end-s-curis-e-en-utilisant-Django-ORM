from rest_framework import routers
from . import views
from django.urls import path, include

router=routers.DefaultRouter()
router.register('contrat', viewset=views.ContratList)

urlpatterns = [
    path('', include(router.urls)),
]
