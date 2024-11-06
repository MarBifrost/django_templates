from django.contrib.auth.views import LoginView
from django.http import HttpResponseNotAllowed
from django.shortcuts import render, get_object_or_404, redirect
from .forms import RegistrationForm, UserCreationForm, LoginForm
from .models import Product, Category
from order.models import Cart, CartItem
from django.db.models import Q
from django.core.paginator import Paginator
from django.contrib.auth import login, authenticate
from django.contrib import messages

# Create your views here.


from django.shortcuts import render, get_object_or_404
from django.views import View
from .models import Product, Category
from order.models import Cart, CartItem
from django.db.models import Q
from django.core.paginator import Paginator


class StoreView(View):
    def get(self, request):
        products = Product.objects.all()
        query = request.GET.get('q')

        if query:
            keywords = query.split()
            query_filter = Q()
            for keyword in keywords:
                query_filter &= Q(product_name__icontains=keyword)
            products = Product.objects.filter(query_filter)

            return render(request, 'shop/shop.html', {'products': products})

        context = {
            'products': products,
            # 'cart': cart,
            # 'cart_items': cart_items,
            # 'total_quantity': total_quantity,
        }
        return render(request, 'index/index.html', context)


class ContactView(View):
    def get(self, request):
        return render(request, 'contact/contact.html')


class ShopView(View):
    def get(self, request):
        products = Product.objects.all()
        categories = Category.objects.all()
        paginator = Paginator(products, 1)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)


        content = {
            'page_obj': page_obj,
            'categories': categories,

        }
        return render(request, 'shop/shop.html', content)


class ShopDetailsView(View):
    def get(self, request):
        return render(request, 'shop/shop-details.html')


class CategoryView(View):
    def get(self, request, slug):
        category = get_object_or_404(Category, slug=slug)
        products = Product.objects.filter(category_name=category)

        context = {
            'category': category,
            'products': products,
        }

        return render(request, 'shop/shop.html', context)


class Registration(View):

    def post(self, request, *args, **kwargs):
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "რეგისტრაცია წარმატებულია!")
            return redirect('accounts:profile')
        else:
            messages.error(request, form.errors)
        form = RegistrationForm()
        return render(request, 'registration/registration.html', {'form': form})


    def get(self, request):
        form = RegistrationForm()
        return render(request, 'registration/registration.html', {'form': form})



class CustomLoginView(LoginView):
    form_class = LoginForm

    def post(self, request, *args, **kwargs):
        form = self.get_form()
        if form.is_valid():
            username=form.cleaned_data['username']
            password=form.cleaned_data['password']

            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('store:store')
            else:
                messages.error(request, "არასწორი მონაცემები")
                return self.form_invalid(form)
        else:
            messages.error(request, "არასწორი მონაცემები")
            return self.form_invalid(form)