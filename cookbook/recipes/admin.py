from django.contrib import admin

from .models import *

admin.site.register(Product)
admin.site.register(Recipe)
admin.site.register(RecipeProduct)
