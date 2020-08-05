from django.shortcuts import render, redirect
from django.contrib.auth.hashers import make_password,check_password
from django.views import View
from store.models.customer import Customer


# Create your views here.
class SignUp(View):
    def get(self,request):
        return render(request, 'orders/signup.html')

    def post(self, request):
        name = request.POST['fname']
        lname = request.POST['lname']
        email = request.POST['email']
        phone = request.POST['phone']
        password = request.POST['password']
        cpassword = request.POST['cpassword']
        value = {'fname': name, 'lname': lname,
                 'email': email, 'phone': phone, }
        customer = Customer(first_name=name, last_name=lname,
                            email=email, phone=phone, password=password)
        error = ''
        error = self.validateCustomer(customer, cpassword)
        if not error:
            customer.password = make_password(customer.password)
            customer.register()
            return redirect('home')
        else:
            return render(request, 'orders/signup.html', {'error': error, 'value': value})

    def validateCustomer(self,customer, cpassword):
        error = ''
        if not customer.first_name:
            error = "First Name Required !!"
        elif len(customer.first_name) < 4:
            error = "First Name Must be 4 char long"
        elif not customer.last_name:
            error = "Last Name Required !!"
        elif len(customer.last_name) < 4:
            error = "Last Name Must be 4 char long"
        elif not customer.phone:
            error = "Phone number Required !!"
        elif len(customer.phone) < 10:
            error = "Phone number be 10 char Long"
        elif not customer.password:
            error = "password Required !! Must be 6 char long"
        elif len(customer.password) < 6:
            error = "Password Must be 6 char long"
        elif customer.password != cpassword:
            error = "password not match"
        elif customer.isExists():
            error = "Email Address Already Registered.."
        return error


        
        
