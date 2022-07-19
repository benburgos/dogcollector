from django.contrib import admin
from .models import Dog, FavoriteTreat, Meal, Photo

admin.site.register(Dog)
admin.site.register(FavoriteTreat)
admin.site.register(Meal)
admin.site.register(Photo)
