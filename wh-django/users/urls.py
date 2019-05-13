from django.urls import path, include
from . import views
from rest_framework import routers

# registers REST api basic urls structure
router = routers.DefaultRouter()
router.register('users', views.UserView)

urlpatterns = [
	path('', include(router.urls)),
]