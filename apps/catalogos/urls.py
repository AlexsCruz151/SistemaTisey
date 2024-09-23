from django.urls import path, include

urlpatterns = [

    path('departamentos/', include('apps.catalogos.departamentos.urls')),
    path('municipios/', include('apps.catalogos.municipios.urls')),
]