"""
URL configuration for django46 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings

from products.views import home_page, get_product_category_page, MyLoginView, logout_view, search_product

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home_page, name='home'),
    path('shop/<int:pk>', get_product_category_page, name='category_page'),
    path('login', MyLoginView.as_view(), name='login'),
    path('logout', logout_view, name='logout'),
    path('search', search_product, name='search-product'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
