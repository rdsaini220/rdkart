from django.shortcuts import render, redirect
from django.http import HttpResponse
from store.models.product import Product
from store.models.category import Category
from django.views import View


# Create your views here.
class Index(View):
    def post(slef, request):
        product = request.POST.get('product_name')
        remove = request.POST.get('product_remove')
        cart = request.session.get('cart')
        if cart:
            quantity = cart.get(product)
            if quantity:
                if remove:
                    if quantity <= 1:
                        cart.pop(product)
                    else:
                        cart[product] = quantity-1
                else:
                    cart[product] = quantity+1

            else:
                cart[product] = 1
        else:
            cart = {}
            cart[product] = 1
        request.session['cart'] = cart
        print('cart value: ',request.session['cart'])
        return redirect('home')

    def get(self,request):
        cart = request.session.get('cart')
        if not cart:
            request.session['cart'] = {}
        products = ''
        # request.session.get('cart').clear()
        cate = Category.objects.all()
        categoryID = request.GET.get('category')
        if categoryID:
            products = Product.get_all_products_by_categoryid(categoryID)
        else:
            products = Product.get_all_products()
        context = {'products': products, 'category': cate}
        print('get user : ', request.session.get('email'))
        return render(request,'index.html',context)



