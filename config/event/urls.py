from rest_framework import routers
from . import views
from django.urls import path, include

router=routers.DefaultRouter()
router.register('event', viewset=views.EventList, basename='event')

urlpatterns = [
    path('', include(router.urls)),
]
