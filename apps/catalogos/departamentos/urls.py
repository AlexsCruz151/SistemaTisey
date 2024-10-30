# from django.urls import path, include
# from rest_framework.routers import DefaultRouter
# from .views import DepartamentoModelViewSet
#
# router = DefaultRouter()
# router.register('', DepartamentoModelViewSet, basename='departamento')
#
# urlpatterns = [
#     path('', include(router.urls)),
# ]
from django.urls import path
from .views import DepartamentoApiView,DepartamentoDetails

urlpatterns = [
    path('', DepartamentoApiView.as_view()),  # Para listar o crear departamentos
    path('<int:pk>', DepartamentoDetails.as_view()),  # Para operaciones GET, PUT, PATCH, DELETE
]

