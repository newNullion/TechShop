from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView
from django.views.generic.edit import CreateView
from django.contrib.auth.views import LoginView
from .models import Category, Product, ProductOffer
from .forms import AddProductForm, LogForm, RegForm
from django.urls import reverse_lazy



class MainView(ListView):
    template_name = 'main.html'
    model = Category
    context_object_name = 'categories'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['product_offers'] = ProductOffer.objects.all()
        return context



class ProductDetailView(DetailView):
    template_name = 'product.html'
    model = Product
    context_object_name = 'product'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        return context



class CategoryDetailView(DetailView):
    template_name = 'category.html'
    model = Category
    context_object_name = 'category'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['products'] = self.object.products.all()
        context['categories'] = Category.objects.all()
        return context


class AuthLoginView(LoginView):
    template_name = 'registrations/login.html'
    form_class = LogForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        return context


class RegView(CreateView):
    template_name = 'registrations/reg.html'
    form_class = RegForm
    success_url = reverse_lazy('login')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        return context



class HelpView(TemplateView):
    template_name = 'help.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        return context



class AddProductView(CreateView):
    template_name = 'add_product.html'
    form_class = AddProductForm
    success_url = reverse_lazy('main')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        return context