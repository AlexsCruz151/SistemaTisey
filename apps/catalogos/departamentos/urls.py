from django.urls import path
from .views import DepartamentoApiView

app_name = "departamentos"

urlpatterns = [
    path('', DepartamentoApiView.as_view(), name="departamento"),
]