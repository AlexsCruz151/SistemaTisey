from django.urls import path
from .views import MunicipiosApiView

app_name = "municipios"

urlpatterns = [
    path('', MunicipiosApiView.as_view(), name="municipios"),
]