from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import DepartamentoModelViewSet

router = DefaultRouter()
router.register('', DepartamentoModelViewSet, basename='departamento')

urlpatterns = [
    path('', include(router.urls)),
]
