from rest_framework import routers
from . import views
from django.urls import path, include

router=routers.DefaultRouter()
router.register('client', viewset=views.ClientList, basename='client')
router.register('user', viewset=views.UserList, basename='user')


urlpatterns = [
    path('', include(router.urls)),
]
