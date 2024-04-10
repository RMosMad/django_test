from django.contrib import admin

from .models import News



# admin.site.register(News)

@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('headline',)}


