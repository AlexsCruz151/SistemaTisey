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
from .views import DepartamentoViewSet #,DepartamentoActivarView
from .ViewSet import *

router = DefaultRouter()
router.register(r'departamentos', DepartamentoViewSet, basename='departamento')
#router.register(r'departamentosS', DepartamentoViewSetES, basename='departamentoSSS')
urlpatterns = [
    path('', include(router.urls)),
    #path('<int:pk>/activarDepartamento/', DepartamentoActivarView.as_view(), name='activar-departamento'),
]
