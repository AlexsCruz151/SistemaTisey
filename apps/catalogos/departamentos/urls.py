# from django.urls import path
# from .views import DepartamentoApiView
#
# app_name = "departamentos"
#
# urlpatterns = [
#     #path('', DepartamentoApiView.as_view(), name="departamento"),
#     path('<str:pk>/', DepartamentoApiView.as_view()),
# ]

from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import DepartamentoViewSet

router = DefaultRouter()
router.register(r'departamentos', DepartamentoViewSet, basename='departamento')

urlpatterns = [
    path('', include(router.urls)),
]
