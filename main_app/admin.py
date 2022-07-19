from django.contrib import admin
from .models import Dog, FavoriteTreat, Meal

admin.site.register(Dog)
admin.site.register(FavoriteTreat)
admin.site.register(Meal)
