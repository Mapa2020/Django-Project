from django.shortcuts import render, redirect
from django.contrib import messages

from .forms import RegisterForm
from django.contrib.auth import authenticate, login, logout
from categorias.models import Categoria, Producto

# Create your views here.

def home(request):
    return render(request, "FINAL_APP/home.html",{'title': 'Inicio'})

def categorias(request):
    productos= Producto.objects.all()
    
    return render(request, "FINAL_APP/categorias.html",{'title': 'Categoria','productos':productos})

def acerca(request):
     return render(request, "FINAL_APP/acerca.html",{'title': 'Acerca de'})

def contacto(request):
    return render(request, "FINAL_APP/contacto.html",{'title': 'Contacto'})

def nuevo(request):           
    return render(request, "FINAL_APP/nuevo.html",{
                            'title': 'Nuevo Producto'})

def registro(request):
    register_form = RegisterForm()
    if request.method == 'POST':
        register_form = RegisterForm(request.POST)
        
        if register_form.is_valid():
            register_form.save()
            messages.success(request, 'Registro Exitoso')
            return redirect('Home')
            
    return render(request, "FINAL_APP/registro.html",{ 
                            'title': 'Registro',
                            'register_form': register_form})

def login_page(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        user = authenticate(request, username=username, password= password)
        if user is not None:
            login(request, user)
            return redirect('Home')
        else:
            messages.warning(request, 'No Identificado Correctamente')
    
    return render(request, "FINAL_APP/login.html", {
                            'title': 'Identificate'})
    
def logout_user(request):
     logout(request) 
     return redirect('Login')  