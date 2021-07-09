from django.contrib import admin
from .models import Categoria, Producto, Carrito

class CategoriaAdmin(admin.ModelAdmin):
    readonly_fields = ('created',)

class ProductoAdmin(admin.ModelAdmin):
    readonly_fields = ('user', 'created')
    
    def save_model(self, request, obj, form, change):
        if not obj.user_id:
            obj.user_id = request.user.id
        
        obj.save()    
        

# Register your models here.
admin.site.register(Categoria, CategoriaAdmin)
admin.site.register(Producto,ProductoAdmin)
admin.site.register(Carrito)

title = "Proyecto WEB DJANGO"
subtitle = "Panel de Gestión"

#Configuracion del Panel
admin.site.site_header = title
admin.site.site_title = title
admin.site.index_title = subtitle