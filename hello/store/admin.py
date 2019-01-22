from django.contrib import admin
from .models import Item, Operation
# Register your models here.


@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    list_display = ('name', 'qty', 'city', 'modify_date', 'who_does')


@admin.register(Operation)
class OperationAdmin(admin.ModelAdmin):
    list_display = ('id', 'item', 'operated_time')

