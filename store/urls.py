from django.urls import path
from .views.home import Index
from .views.signup import SignUp
from .views.login import Login, Logout
from .views.pro_cart import ProductCart
from .views.checkout import CkeckOut
from .views.orders import OrdersView
from .middleware.auth import auth_middleware

urlpatterns = [
    path('', Index.as_view(), name='home'),
    path('signup/', SignUp.as_view(), name='signup'),
    path('login/', Login.as_view(), name='login'),
    path('logout/', Logout, name='logout'),
    path('cart/', auth_middleware(ProductCart.as_view()), name='cart'),
    path('check-out/', CkeckOut.as_view(), name='check-out'),
    path('orders/', auth_middleware(OrdersView.as_view()), name='orders'),
] 
