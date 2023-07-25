from django.shortcuts import render, redirect, HttpResponse
from Store import models, forms as store_forms
from . import forms

product = None

Models = {
       'products':models.Product.objects,
       'navbar':models.NavSlider.objects,
       'images':models.ProdImages.objects,
       'categories':models.Category.objects,
       'news':models.News.objects,
       'order':models.Order.objects,
    }
Forms = {
    'products':forms.ProductForm,
    'navbar':forms.NavForm,
    'images':forms.ImagesForm,
    'categories':forms.CatForm,
    'news':forms.NewsForm,
    'order':store_forms.OrderForm,
}

def dashboard(request):
    products = models.Product.objects.all()
    cat = models.Category.objects.all()
    Images = models.ProdImages.objects.all()
    news = models.News.objects.all()
    nav = models.NavSlider.objects.all()
    orders = models.Order.objects.all()
    all = [products, Images, news, nav, cat, orders]

    
    context = {
        'products': products,
        'cats': cat,
        'Images': Images,
        'news': news,
        'navs': nav,
        'orders':orders,
        'all':all,
        
    }

    return render(request, 'home.html', context)





def form (request, slug):

    global product, Forms, Models

    slug = slug.lower()
    form = Forms[slug]()
    P_form = Forms[slug]
    fields = [str(x) for x in form.fields]


    if request.method == 'POST':
        form = P_form(request.POST)
        if form.is_valid():
            form.save()
            # Models[slug].create(**parsekwargs(fields, form.cleaned_data))
            fields.clear()
            return redirect('/admin')
        
    context = {'form': form, 'name':slug, 'update':False}
   
    return render(request, 'form.html', context)    


def alter(request, slug):

    model, id = slug.split('_')
    entity = Models[model.lower()].get(id=id)
    form = Forms[model.lower()](instance=entity)      

    if request.method == 'POST':
        print(str(request)*100)
        form = Forms[model.lower()](request.POST, instance=entity)
        if form.is_valid():
            form.save()
            # create(**parsekwargs(fields, form.cleaned_data))
            
            return redirect('/admin')
        
    context = {'form': form, 'name':model, 'update':True, 'id':id}

    return render(request, 'form.html', context)
    # return HttpResponse("hello")
   

def delete(request, slug):
    model, id = slug.split('_')
    entity = Models[model.lower()].get(id=id)
    entity.delete()
    return redirect('/admin')



# =====================================
# These functions are not for rendering
# =====================================

def parsekwargs(array, cleaned_data):
    kwargs = {}
    for field in array:
        kwargs[field] = cleaned_data[field]       

    return kwargs



def detectDivergents(array1, array2):
    Divergents = []
    for index, item in enumerate(array1):
        if item != array2[index]:
            Divergents.append(str(item))
    return Divergents