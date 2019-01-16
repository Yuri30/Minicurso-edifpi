from django.urls import include, path

from . import views

app_name = 'appCadastro'

urlpatterns = [
    path('api/', include('appCadastro.api.urls')),
]