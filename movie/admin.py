from django.contrib import admin

from .models import Movies, Review, Classification, Genre, Director



# admin.site.register(Movies)
admin.site.register(Review)
admin.site.register(Classification)
admin.site.register(Genre)
admin.site.register(Director)


@admin.register(Movies)
class MoviesAdmin(admin.ModelAdmin):
    list_display = ['title', 'date', 'genre', 'clasificacion', 'create_uid_movies', 'write_uid_movies', 'create_date']
    list_filter = ['title', 'date', 'genre', 'clasificacion']
    search_fields = ['title', 'date', 'genre', 'clasificacion']
    raw_id_fields = ['directors']
    ordering = ['create_date']











