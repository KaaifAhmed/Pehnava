ADMIN_ORDERING = (
    ('Store', 
        (
         'Pending_Order', 
         'Delivered_Order', 
         'Customer', 
         'Product', 
         'Size', 
         'ProductImagery', 
         'Category', 
         'News' 
         ,'Banner'
        )
    ),
    ('auth', 
        (
        'User', 
        'Group'
        )
        ),
)
from django.contrib import admin

def get_app_list(self, request, app_label=None):
    app_dict = self._build_app_dict(request, app_label)
    
    if not app_dict:
        return
        
    NEW_ADMIN_ORDERING = []
    if app_label:
        for ao in ADMIN_ORDERING:
            if ao[0] == app_label:
                NEW_ADMIN_ORDERING.append(ao)
                break
    
    if not app_label:
        for app_key in list(app_dict.keys()):
            if not any(app_key in ao_app for ao_app in ADMIN_ORDERING):
                app_dict.pop(app_key)
    
    app_list = sorted(
        app_dict.values(), 
        key=lambda x: [ao[0] for ao in ADMIN_ORDERING].index(x['app_label'])
    )
     
    for app, ao in zip(app_list, NEW_ADMIN_ORDERING or ADMIN_ORDERING):
        if app['app_label'] == ao[0]:
            for model in list(app['models']):
                if not model['object_name'] in ao[1]:
                    app['models'].remove(model)
        app['models'].sort(key=lambda x: ao[1].index(x['object_name']))
    return app_list

admin.AdminSite.get_app_list = get_app_list


from django.contrib import admin
from . import models



# admin.site.register(models.Product)
admin.site.register(models.Category)
admin.site.register(models.Banner)
admin.site.register(models.News)
admin.site.register(models.ProductImagery)
# admin.site.register(models.Pending_Order)
admin.site.register(models.Delivered_Order)
admin.site.register(models.Customer)
admin.site.register(models.Size)




class PendingOrderAdmin(admin.ModelAdmin):
    list_display = ('firstname', 'lastname', 'id', 'ordered_date', 'town', 'city')
    list_filter = ('customer', 'placement_date')
    search_fields = ('id', 'firstname', 'lastname', 'email', 'phone', 'customer')

    class Meta:
        verbose_name = "Order (Pending)"
        verbose_name_plural = "Orders (Pending)"

    def __str__(self):
        return f"Order id: {self.id},  \"{self.firstname}-{self.lastname}\" ordered on {str(self.placement_date)[:10]}"



class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'qty', 'price', 'category', 'tag', 'id')
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



admin.site.register(models.Product, ProductAdmin)
admin.site.register(models.Pending_Order, PendingOrderAdmin)
