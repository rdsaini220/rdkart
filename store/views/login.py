from django.shortcuts import render, redirect ,HttpResponseRedirect
from django.contrib.auth.hashers import make_password,check_password
from django.views import View
from store.models.customer import Customer


# Create your views here.
class Login(View):
    return_url = ''
    def get(self,request):
        Login.return_url = request.GET.get('return_url')
        return render(request, 'orders/login.html')

    def post(self, request):
        email = request.POST['email']
        password = request.POST['password']
        customer = Customer.get_customer_by_email(email)
        error = ''
        if customer:
            flag = check_password(password, customer.password)
            if flag:
                request.session['customer'] = customer.id
                request.session['email'] = customer.email
                if Login.return_url:
                    return HttpResponseRedirect(Login.return_url)
                else:
                    Login.return_url = None
                    return redirect('home')
            else:
                error = 'Email or Password invalid !!'
        else:
            error = 'Email or Password invalid !!'
        return render(request, 'orders/login.html', {'error': error})


def Logout(request):
    request.session.clear()
    return redirect('login')

        
        
