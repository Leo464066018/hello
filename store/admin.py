from django.contrib import admin
from .models import Item, Operation, PostManage, Box
# Register your models here.


@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    list_display = ('name', 'qty', 'city', 'who_does')


@admin.register(Operation)
class OperationAdmin(admin.ModelAdmin):
    list_display = ('id', 'item', 'operated_time', 'note')


@admin.register(PostManage)
class PostManageAdmin(admin.ModelAdmin):
    list_display = ('post_num', 'server_type', 'server_num', 'post_date', 'note_text')


@admin.register(Box)
class BoxAdmin(admin.ModelAdmin):
    list_display = ('box_id', 'sim_card')
