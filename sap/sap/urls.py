from django.contrib import admin
from django.urls import path

from webapp.views import bienvenido, despedirse, contactos

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', bienvenido),
    path('despedida/', despedirse),
    path('contacto/', contactos),
]
