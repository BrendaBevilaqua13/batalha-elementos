from django.contrib import admin
from .models import Carta


@admin.register(Carta)
class Carta(admin.ModelAdmin):
    list_display = ['elemento',]