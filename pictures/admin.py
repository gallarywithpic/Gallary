from django.contrib import admin
 
from .models import Pictures
 
class PicturesAdmin(admin.ModelAdmin):
    list_display = ("name", "state",)
 
admin.site.register(Pictures, PicturesAdmin)