from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="Home"),
    path('categorias', views.categorias, name="Categorias"),
    path('acerca', views.acerca, name="Acerca"),
    path('contacto', views.contacto, name="Contacto"),
    path('nuevo', views.nuevo, name="Nuevo"),
    path('registro', views.registro, name="Registro"),
    path('login', views.login_page, name="Login"),
    path('logout', views.logout_user, name="Logout"),
]