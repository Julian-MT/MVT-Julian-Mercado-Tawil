from django.urls import path, include
from Entregable.views import inicio, familiares


urlpatterns = [
    path('', inicio),
    path('familiares/', familiares)
]
