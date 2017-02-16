from django.contrib import admin

# Register your models here.

from .models import Palabra, Intento, Reportada, Rendicion

class IntentoAdmin(admin.ModelAdmin):
    palabra = Palabra
    list_display = ['palabra', 'intentos', 'fecha']

    def get_name(self, obj):
        return obj.word.name
    get_name.admin_order_field  = 'word'  #Allows column order sorting
    get_name.short_description = 'Palabra'  #Renames column head

class RendicionAdmin(admin.ModelAdmin):
    palabra = Palabra
    list_display = ['palabra', 'intentos', 'fecha']

    def get_name(self, obj):
        return obj.word.name
    get_name.admin_order_field  = 'word'  #Allows column order sorting
    get_name.short_description = 'Palabra'  #Renames column head

admin.site.register(Palabra)
admin.site.register(Intento, IntentoAdmin)
admin.site.register(Reportada)
admin.site.register(Rendicion, RendicionAdmin)