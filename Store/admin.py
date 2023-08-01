from django.contrib import admin
from . import models

# Register your models here.
# admin.site.register(models.Product)
admin.site.register(models.Category)
admin.site.register(models.Banner)
admin.site.register(models.News)
admin.site.register(models.ProductImagery)
# admin.site.register(models.Pending_Order)
admin.site.register(models.Delivered_Order)
admin.site.register(models.Customer)
admin.site.register(models.Size)

    # Customizations for Delivered_Order inline admin



class PendingOrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'firstname', 'lastname', 'email', 'phone', 'placement_date', 'delivered')
    list_filter = ('customer', 'placement_date')
    search_fields = ('id', 'firstname', 'lastname', 'email', 'phone', 'customer')

    class Meta:
        verbose_name = "Order (Pending)"
        verbose_name_plural = "Orders (Pending)"

    def __str__(self):
        return f"Order id: {self.id},  \"{self.firstname}-{self.lastname}\" ordered on {str(self.placement_date)[:10]}"

class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'qty', 'price', 'category', 'tag', 'on_top_product')
    list_filter = ('category', 'on_top_product', 'tag')
    search_fields = ('name', 'tag')
    ordering = ('-id',)

    fieldsets = (
        ('General Information', {
            'fields': ('name', 'qty', 'price', 'slug', 'image', 'category', 'sizes'),
        }),
        ('Tags and Description', {
            'fields': ('tag', 'tag_color', 'desc'),
        }),
        ('Product Options', {
            'fields': ('on_top_product', 'hide'),
        }),
    )

    filter_horizontal = ('sizes',)

    def __str__(self):
        return self.name

# Register the Product model with the custom admin class
admin.site.register(models.Product, ProductAdmin)
admin.site.register(models.Pending_Order, PendingOrderAdmin)