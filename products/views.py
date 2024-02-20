from django.shortcuts import render, redirect

from products.models import Category, ProductModel
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy
from django.contrib.auth import logout



def home_page(request):
    # Собираем все данные категории
    category_info = Category.objects.all()
    product_info = ProductModel.objects.all()
    context = {'categories': category_info, 'products': product_info}
    return render(request, 'index.html', context)


def get_product_category_page(request, pk):
    # categories = Category.objects.get(pk=pk)
    products = ProductModel.objects.all()
    product_categories = Category.objects.all()

    context = {'products': products, 'product_categories': product_categories}
    return render(request, 'shop-grid.html', context)

class MyLoginView(LoginView):
    template_name = 'login.html'
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy('home')

def logout_view(request):
    logout(request)
    return redirect('home')

def search_product(request):
    if request.method == 'POST':
        get_product = request.POST.get('search_product')

        try:
            exact_product = ProductModel.objects.get(product_name__icontains=get_product)

            return redirect(f'shop/{exact_product.id}')
        except:
            return redirect('/')