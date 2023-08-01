from django.db import models
from datetime import datetime
from django.utils.safestring import mark_safe

class Customer(models.Model):

    id = models.BigAutoField(primary_key=True)
    email = models.EmailField(max_length=50, blank=True)
    phone = models.CharField(max_length=12, blank=True)
    firstname = models.CharField(max_length=50, blank=True)
    lastname = models.CharField(max_length=50, blank=True)
    address = models.CharField(max_length=100, blank=True)
    town = models.CharField(max_length=100, blank=True)
    city = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return f"{self.firstname}-{self.lastname}"
    

class News(models.Model):
    content = models.CharField(max_length=50)
    hide = models.BooleanField(default=False)
    html_id = "News"


    class Meta:
        verbose_name_plural = "News"

    def __str__(self):
        return self.content
    

class Category(models.Model):
    name = models.CharField(max_length=50)
    html_id = "Categories"
    image = models.ImageField(upload_to="media",blank=True, null=True)

    class Meta:
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.name.capitalize()
    

class Banner(models.Model):

    image = models.ImageField(upload_to="media",blank=True, null=True)
    responsified_image = models.ImageField(upload_to="media",blank=True, null=True)
    html_id = "Navbar"

    def __str__(self):
        return self.image.url


class Size(models.Model):
    size = models.CharField(blank=True, max_length=10, null=True)

    class Meta:
        verbose_name = "Product Size"
        verbose_name_plural = "Product Sizes"
     
    def __str__(self):
        return f"{self.size[0]}"
    




class Product(models.Model):

    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    qty = models.IntegerField()
    price = models.IntegerField()
    slug = models.CharField(max_length=50)
    image = models.ImageField(upload_to="media", null=True)

    choices = []
    for x in Category.objects.all():
        choices.append((x.name, x.name))
    choices = tuple(choices)

    category = models.CharField(choices=choices, max_length=13, null=True)
    sizes = models.ManyToManyField(Size, blank=True, null=True)

    tag = models.CharField(max_length=50)
    tag_color = models.CharField(max_length=20)
    desc = models.CharField(max_length=9999)

    on_top_product = models.BooleanField(default=False)
    hide = models.BooleanField(default=False)
    html_id = "Products"

    def __str__(self):
        return self.name




class ProductImagery (models.Model):

    id = models.AutoField(primary_key=True)
    
    name = models.ForeignKey(Product, on_delete=models.CASCADE)
    image = models.ImageField(upload_to="media", null=True)
    html_id = "Images"

    class Meta:
        verbose_name = "Imagery"
        verbose_name_plural = "Imageries"

    def __str__(self):
        return str(self.name)



class Pending_Order (models.Model):
    id = models.AutoField(primary_key=True)
    delivered = models.BooleanField(default=False, blank=True)
    email = models.EmailField(max_length=50, blank=True)
    phone = models.CharField(max_length=12, blank=True)
    firstname = models.CharField(max_length=50, blank=True)
    lastname = models.CharField(max_length=50, blank=True)
    address = models.CharField(max_length=100, blank=True)
    town = models.CharField(max_length=100, blank=True)
    city = models.CharField(max_length=100, blank=True)
    payment = models.CharField(max_length=30, blank=True)
    delivery = models.CharField(max_length=30, blank=True)
    cart = models.TextField(null=True, blank=True)
    html_id = 'Order'
    placement_date = models.DateTimeField(auto_now_add=True, null=True)
    customer = models.ForeignKey(Customer, blank=True, null=True, on_delete=models.CASCADE)

    class Meta:
            verbose_name = "Order (Pending)"
            verbose_name_plural = "Orders (Pending)"

    
    def __str__(self):
        return f"Order id: {self.id},  \"{self.firstname}-{self.lastname}\" ordered on {str(self.placement_date)[:10]}"


class Delivered_Order(models.Model):

    cart = models.TextField(null=True, blank=True)
    payment = models.CharField(max_length=30, blank=True)
    delivery = models.CharField(max_length=30, blank=True)
    ordered_date = models.CharField(max_length=20)
    delivered_date = models.DateTimeField(auto_now_add=True, null=True)
    customer = models.ForeignKey(Customer, null=True, on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Order (Delivered)"
        verbose_name_plural = "Orders (Delivered)"

    def __str__(self):
        return f"{self.customer.firstname}-{self.customer.lastname}'s ordered was delivered on {str(self.delivered_date)[:10]}"


