from django.contrib import admin
from . import models

# Register your models here.
admin.site.register(models.Product)
admin.site.register(models.Category)
admin.site.register(models.NavSlider)
admin.site.register(models.News)
admin.site.register(models.ProdImages)
admin.site.register(models.Order)
