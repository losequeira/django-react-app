from django.urls import include, path
from rest_framework import routers

from . import views

router = routers.DefaultRouter()
router.register(r'students', views.StudentView, 'student')

urlpatterns = [
    path('', include(router.urls)),
]