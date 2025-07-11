from .models import Product, Category, ProductOffer
from django.forms import ModelForm
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.models import User



class LogForm(AuthenticationForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs.update({'placeholder': ' '})


class RegForm(UserCreationForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs.update({'placeholder': ' '})
            field.help_text = ''


class AddProductForm(ModelForm):
    class Meta:
        model = Product
        fields = ('name', 'price', 'description', 'file', 'category')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs.update({'placeholder': ' '})



# def __init__(self, *args, **kwargs):
#     super().__init__(*args, **kwargs)
#     for field in self.fields.values():
#         field.widget.attrs.update({'placeholder': ' '})
