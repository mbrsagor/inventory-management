from django.contrib import admin

from product.models.category import Category
from product.models.tag import Tag


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'parent', 'created_at', 'update_at']
    list_display_links = ['name', 'parent']
    # list_editable = ['name', 'parent']
    list_filter = ['name']
    list_per_page = 8


admin.site.register(Category, CategoryAdmin)
admin.site.register(Tag)
