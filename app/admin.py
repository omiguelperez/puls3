from django.contrib import admin
from .models import Agregador, Categoria, Enlace

# Register your models here.

class EnlaceInline(admin.StackedInline):
    model = Enlace
    extra = 2
    raw_id_fields = ('usuario',)

class EnlaceAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'enlace', 'categoria', 'imagen_voto', 'es_popular',)
    list_filter = ('categoria', 'usuario',)
    search_fields = ('categoria__titulo', 'usuario__email',)
    list_editable = ('titulo', 'enlace', 'categoria',)
    list_display_links = ('es_popular', 'imagen_voto',)
    raw_id_fields = ('categoria', 'usuario',)

    def imagen_voto(self, enlace):
        url = enlace.mis_votos_en_imagen_rosada()
        tag = '<img src="%s">' % url
        return tag
    imagen_voto.allow_tags = True
    imagen_voto.admin_order_field = 'votos'

class CategoriaAdmin(admin.ModelAdmin):
    inlines = (EnlaceInline,)

class AgregadorAdmin(admin.ModelAdmin):
    filter_horizontal = ['enlaces']

admin.site.register(Agregador, AgregadorAdmin)
admin.site.register(Categoria, CategoriaAdmin)
admin.site.register(Enlace, EnlaceAdmin)
