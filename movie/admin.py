from django.contrib import admin
from .models import Movie, Genre, Actor, Director


class MovieEditAdmin(admin.ModelAdmin):
    readonly_fields = ('is_production',)
    exclude = ('is_production',)


admin.site.register(Movie, MovieEditAdmin)
admin.site.register((Genre, Actor, Director,))
