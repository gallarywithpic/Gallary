from django.contrib import admin
from .models import Pictures
 
class PicturesAdmin(admin.ModelAdmin):
    list_display = ("name", "culka",)
 
admin.site.register(Pictures, PicturesAdmin)