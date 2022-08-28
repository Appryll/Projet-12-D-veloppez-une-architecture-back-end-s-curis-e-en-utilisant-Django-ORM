from rest_framework import routers
from . import views
from django.urls import path, include

router=routers.DefaultRouter()
router.register('client', viewset=views.ClientList)
router.register('user', viewset=views.UserList)


urlpatterns = [
    path('', include(router.urls)),
]
