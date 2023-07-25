from django.db import models




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



class Order (models.Model):
    id = models.AutoField(primary_key=True)
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

    def __str__(self):
        return f"Order id: {self.id}"

