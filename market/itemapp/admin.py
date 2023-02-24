from django.contrib import admin
from .models import Item


@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name', 'description', 'price', 'created_at', 'updated_at')
    list_filter = ('deleted', 'created_at')
    ordering = ('-pk', 'deleted', 'created_at')
    list_per_page = 20
    search_fields = ('name', 'description', 'price')
    actions = ('mark_as_delete', 'mark_as_active',)

    def mark_as_delete(self, request, queryset):
        queryset.update(deleted=True)

    mark_as_delete.short_description = 'Mark as deleted'

    def mark_as_active(self, request, queryset):
        queryset.update(deleted=False)

    mark_as_active.short_description = 'Remove the mark for deletion'
