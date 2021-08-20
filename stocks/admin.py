from django.contrib import admin

from .models import Symbol, Stock

# Register your models here.
admin.site.register(Symbol)
admin.site.register(Stock)