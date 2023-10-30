from django.contrib import admin

# NOTE: Tenemos que importar los modelos con los que vamos a trabajar:
from e_commerce.models import *

# Register your models here.

# NOTE: Aquí personalizamos los campos en el Django Admin.

@admin.register(Comic)
class ComicsAdmin(admin.ModelAdmin):
    # NOTE: Para seleccionar los campos en la tabla de registros
    list_display = ('marvel_id', 'title', 'stock_qty', 'price')

    # NOTE: Filtro lateral de elementos:
    list_filter= ('marvel_id','title')
    
    # NOTE: Buscador de elementos en la columna:
    search_fields = ['title']

    # NOTE: Para seleccionar los campos en el registro. 
    # fields = ('marvel_id', 'title', 'stock_qty')

    # NOTE: Genera un campo desplegable con los registros seleccionados.
    fieldsets = (
        (None, {
            'fields': ('marvel_id', 'title', 'stock_qty')
        }),
        ('Advanced options', {
            'classes': ('collapse',),
            'fields': ('description','price', 'picture'),
        }),
    )
    pass


@admin.register(WishList)
class WishListsAdmin(admin.ModelAdmin):
    #NOTE: Para seleccionar los campos en la tabla de registros
    list_display2 = ('id', 'user', 'comic', 'favorite')

    #NOTE: Filtro lateral de elementos:
    list_filter2= ('id','user','comic')
    
    #NOTE: Buscador de elementos en la columna:
    search_fields2 = ['comic']

    #NOTE: Para seleccionar los campos en el registro. 
    #fields = ('id', 'comic', 'wished_qty')

    #NOTE: Genera un campo desplegable con los registros seleccionados.
    fieldsets2 = (
        (None, {
            'fields': ('id', 'user', 'comic','favorite')
        }),
        ('Advanced options', {
            'classes': ('collapse',),
            'fields': ('cart','wished_qty', 'bought_qty'),
        }),
    )
    pass

