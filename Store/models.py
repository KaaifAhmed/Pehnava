from django.db import models
from datetime import datetime

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
    name = models.CharField(max_length=50)
    hide = models.BooleanField(default=False)
    html_id = models.CharField(max_length=255, default='News', blank=True)


    class Meta:
        verbose_name_plural = "News"

    def __str__(self):
        return self.name
    

class Category(models.Model):
    category = models.CharField(max_length=50)
    html_id = "Categories"
    url = models.ImageField(blank=True, null=True)

    def __str__(self):
        return self.category.capitalize()
    

class NavSlider(models.Model):

    name = models.URLField()
    html_id = models.CharField(max_length=255, default='Navbar', blank=True)

    def __str__(self):
        return self.name



class Product(models.Model):

    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    tag = models.CharField(max_length=50)
    tag_color = models.CharField(max_length=20)
    desc = models.CharField(max_length=9999)
    qty = models.IntegerField()
    price = models.IntegerField()
    raw_slug = models.CharField(max_length=50)
    img = models.URLField()
    on_top_product = models.BooleanField(default=False)
    hide = models.BooleanField(default=False)
    html_id = models.CharField(max_length=255, default='Products', blank=True)

    choices = []
    for x in Category.objects.all():
        choices.append((x.category, x.category))
    choices = tuple(choices)

    cat = models.CharField(choices=choices, max_length=13)
    

    def __str__(self):
        return self.name



class ProdImages (models.Model):

    id = models.AutoField(primary_key=True)
    
    name = models.ForeignKey(Product, on_delete=models.CASCADE)
    url = models.URLField()
    html_id = models.CharField(max_length=255, default='Images', blank=True)

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
    html_id = models.CharField(max_length=255, default='Order', blank=True)
    created_date = models.DateTimeField(auto_now_add=True, null=True)
    customer = models.ForeignKey(Customer, blank=True, null=True, on_delete=models.CASCADE)

    class Meta:
            verbose_name = "Pending_Order"
            verbose_name_plural = "Pending_Orders"

    
    def __str__(self):
        # time = datetime.strptime(str(self.created_date)[11:16], "%H:%M")
        # format = "%I:%M %p"
        return f"\"{self.firstname}-{self.lastname}\" ordered on {str(self.created_date)[:10]}"


class Delivered_Order(models.Model):

    cart = models.TextField(null=True, blank=True)
    payment = models.CharField(max_length=30, blank=True)
    delivery = models.CharField(max_length=30, blank=True)
    ordered_date = models.CharField(max_length=20)
    delivered_date = models.DateTimeField(auto_now_add=True, null=True)
    customer = models.ForeignKey(Customer, null=True, on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Delivered_Order"
        verbose_name_plural = "Delivered_Orders"

    def __str__(self):
        return f"{self.customer.firstname}-{self.customer.lastname}'s ordered was delivered on {str(self.delivered_date)[:10]}"



