from django import forms
from Store import models




class ProductForm(forms.ModelForm):
    class Meta:
        model = models.Product
        fields = '__all__'
    

class NavForm(forms.ModelForm):
    class Meta:
        model = models.NavSlider
        fields = '__all__'
    

class CatForm(forms.ModelForm):
    class Meta:
        model = models.Category
        fields = '__all__'
    

class ImagesForm(forms.ModelForm):
    class Meta:
        model = models.ProdImages
        fields = '__all__'
    

class NewsForm(forms.ModelForm):
    class Meta:
        model = models.News
        fields = '__all__'
    

