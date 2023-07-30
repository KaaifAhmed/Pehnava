from django.shortcuts import redirect, render, HttpResponse
from .models import NavSlider, News, Product, Category, ProdImages, Pending_Order, Delivered_Order, Customer
from .forms import OrderForm
from django.utils.safestring import mark_safe

# Create your views here.

slides = NavSlider.objects.all()
news = News.objects.all()[0]
top_products = Product.objects.filter(on_top_product=True)
sug_products = Product.objects.all()
new_products = Product.objects.filter(tag="NEW")
cat = Category.objects.all()
imgs = ProdImages.objects.all()
o_id = None


def index(request, id=None):
    global o_id
    shiftOrder(Pending_Order)
    
    
    if id and o_id is None:
        return redirect("/")
    
    if id:
        o_id = None

    return render(request, 'index.html', {
        "slides": slides,
        "news":news,
        "top_products": top_products,
        "sug_products": sug_products,
        "new_products": new_products,
        "category": cat,
        "imgs":imgs,
        "id":id
    })

def product(request, slug):

    products = Product.objects.filter(raw_slug=slug).first()
    images = ProdImages.objects.filter(name=products)
    suggestions = Product.objects.filter(cat=products.cat)
    suggestions = list(suggestions)
    suggestions.remove(products)
    news = News.objects.all()[0]
    s_images = ProdImages.objects.all()
    cat = Category.objects.all()


    return render(request, 'product.html', {
        'product': products,
        # 'product': mark_safe(products),
        'images':images,
        'suggestions':suggestions,
        's_images':s_images,
        'news':news,
        'category':cat,
        'sizes':products.size.all(),
        'colors':products.color.all()
    })

def checkout(request):
    from json import loads
    form = OrderForm()
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            order = {
                'email' : form.cleaned_data['email'],
                'phone' : form.cleaned_data['phone'],
                'firstname' : form.cleaned_data['firstname'],
                'lastname' : form.cleaned_data['lastname'],
                'address' : form.cleaned_data['address'],
                'town' : form.cleaned_data['town'],
                'city' : form.cleaned_data['city'],
                'payment' : form.cleaned_data['payment'],
                'delivery' : form.cleaned_data['delivery'],
                'cart' : form.cleaned_data['cart'],
                'delivered':form.cleaned_data['delivered'],

            }
            customer = Customer.objects.filter(email=order['email'])
            if not customer:
                customer = Customer(
                    email = order['email'],
                    phone = order['phone'],
                    firstname = order['firstname'],
                    lastname = order['lastname'],
                    address = order['address'],
                    town = order['town'],
                    city = order['city']
                )
                customer.save()
                customer = Customer.objects.filter(email=order['email'])
            
            order['customer'] = customer[0]

            _order = Pending_Order(**order)
            _order.save()   
            cart = loads(order.get('cart'))
            val = decrementQunatity(cart['name'], int(cart['qty']))
            
            global o_id
            o_id = _order.id

        return redirect(f"/{_order.id}")
    else:
      
        context = {
            'form':form,
        }
       
        return render(request, 'checkout.html', context)
     


def search(request):

    query : str = request.GET.get('-search')
    print(len(query)>1, query[-2] == '-', query)
    if len(query)>1 and query[-2] == '-':
        catSearchResult = True
        query = query[:-2]
        print(query)
    else:
        catSearchResult = False
    catwise = Product.objects.filter(cat__icontains=query)
    slugwise = Product.objects.filter(raw_slug__icontains=query)
    namewise = Product.objects.filter(name__icontains=query)
    descwise = Product.objects.filter(desc__icontains=query)
    results = catwise.union(slugwise, descwise, namewise)
    imgs = ProdImages.objects.all()
    
    context = {
        'results':results,
        'total':len(results),
        'keyword':query,
        'imgs':imgs,
        'category': Category.objects.all(),
        'isACategory':catSearchResult
    }
    return render(request, 'search.html', context)
    

def tracker(request, product):
    context = {'order':Pending_Order.objects.get(id=product)}

    return render(request, 'tracker.html', context)




# --------------------------
def shiftOrder(orders):
    # print(orders.first())
    delivered_orders = orders.objects.filter(delivered=True)
   
    for delivered in delivered_orders[:]:
        if delivered:
            order = Delivered_Order(
                cart = delivered.cart,
                payment = delivered.payment,
                delivery = delivered.delivery,
                customer = delivered.customer,
                ordered_date = str(delivered.created_date),
            )
            order.save()
            delivered.delete()


def decrementQunatity(of:str, by:int):
    product = Product.objects.filter(name=of).first()
    product.qty -= by
    product.save()

    return Product.objects.filter(name=of).first().qty


# --------------------------



def Kaaif_Panchayat(form):
    Contact_information : list = []
    Shipping_address : list = []
    Delivery_method : list = []
    Payment_Method : list = []

    for i, field in enumerate(form):
        if field.name in ['email', 'phone']:
            Contact_information.append(field)

        elif field.name == 'payment':
            Payment_Method.append(field)

        elif field.name == 'delivery':
            Delivery_method.append(field)

        else:
            Shipping_address.append(field)
    return Contact_information, Shipping_address, Delivery_method, Payment_Method



