from django.contrib import admin
from .models import Flower, Action


class FlowerAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'description', 'image')


admin.site.register(Flower, FlowerAdmin)
admin.site.register(Action)
