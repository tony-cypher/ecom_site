from django.contrib import admin
from.models import Product, Order

admin.site.site_header = 'Ecommerce Site'
admin.site.site_title = 'Cypher Shopping'
admin.site.index_title = 'Manage Shopping'


class ProductAdmin(admin.ModelAdmin):

    def change_category_to_default(self, request, queryset):
        queryset.update(category='default')
    change_category_to_default.short_description = 'Default Category'
    list_display = ('title', 'price', 'discount_price', 'category', 'description',)
    search_fields = ('title',)
    actions = ('change_category_to_default',)
    fields = ('title', 'price',)
    list_editable = ('price', 'category',)


# Register your models here.
admin.site.register(Product, ProductAdmin)
admin.site.register(Order)
