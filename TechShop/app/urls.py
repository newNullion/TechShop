from django.urls import path
from .views import MainView, ProductDetailView, CategoryDetailView, AuthLoginView, AddProductView, HelpView, RegView
from django.contrib.auth.views import LogoutView
from django.conf import settings
from django.conf.urls.static import static



urlpatterns = [
    path('', MainView.as_view(), name='main'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('product/<int:pk>', ProductDetailView.as_view(), name='product'),
    path('category/<int:pk>', CategoryDetailView.as_view(), name='category'),
    path('login/', AuthLoginView.as_view(), name='login'),
    path('help/', HelpView.as_view(), name='help'),
    path('add_product/', AddProductView.as_view(), name='add_product'),
    path('reg/', RegView.as_view(), name='reg'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

