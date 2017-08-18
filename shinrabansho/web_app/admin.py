from django.contrib import admin
from web_app.models import web_app_data

# Register your models here.

class web_app_dataAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'date',)
    list_display_links = ('id', 'title',)

admin.site.register(web_app_data, web_app_dataAdmin)
