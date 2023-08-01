from django.contrib import admin
from . import models

# Register your models here.
admin.site.register(models.Product)
admin.site.register(models.Category)
admin.site.register(models.Banner)
admin.site.register(models.News)
admin.site.register(models.ProductImagery)
admin.site.register(models.Pending_Order)
admin.site.register(models.Delivered_Order)
admin.site.register(models.Customer)
admin.site.register(models.Size)
