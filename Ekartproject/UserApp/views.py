from django.shortcuts import render,redirect
from django.views.generic import TemplateView,CreateView,FormView,DetailView,ListView
from django.contrib.auth.models import User
from AdminApp.models import Products
from django.urls import reverse_lazy
from django.views import View 
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from UserApp.forms import SignUpForm,SigninForm,CartForm,OrderForm
from UserApp.models import Cart,Orders
from django.core.mail import send_mail,settings
from UserApp.decorators import login_required
from django.utils.decorators import method_decorator

# Create your views here.

class Home(TemplateView):
    template_name="index.html"

    def get_context_data(self, **kwargs):
        context=super().get_context_data(**kwargs)
        # print(self.request.user.email)
        print(self.request.user)
        context["products"]=Products.objects.all()
        return context


class SignUpView(CreateView):
    form_class=SignUpForm
    template_name='signup.html'
    model=User
    success_url=reverse_lazy('home_view')
    

    def form_valid(self, form):
        User.objects.create_user(**form.cleaned_data)
        messages.success(self.request,"Registration successfull")
        return redirect("home_view")
    def form_invalid(self,form):
        messages.warning(self.request,"Invalid input")
        return super().form_invalid(form)
    

class SignInView(FormView):
    form_class=SigninForm
    template_name='signin.html'

    def post(self, request, *args, **kwargs):
       uname=request.POST.get("username")
       psw=request.POST.get("password")
       user=authenticate(request,username=uname,password=psw)
       if user:
            if user.is_superuser==1:
                order_count=Orders.objects.filter(status="order-placed").count()
                return render(request,"dashboard.html",{'order':order_count})
            else:
               login(request,user)
               messages.success(request,'Login Successfull')
               return redirect("home_view")
       else:
           messages.warning(request,"Invalid Input")
           return redirect("signin_view")
       

class SignoutView(View):
    def get(self,request):
        logout(request)
        messages.success(request,"Logout successfull")
        return redirect('signin_view')
       
class ProductDetailView(DetailView):
    model=Products
    pk_url_kwarg="id"
    template_name="product_detail.html"
    context_object_name="product"

@method_decorator(login_required,name='dispatch')
class AddToCartView(TemplateView):
    model=Cart
    template_name="add_to_cart.html"

    def get_context_data(self,**kwargs):
        context=super().get_context_data(**kwargs)
        context["product"]=Products.objects.get(id=kwargs.get("id"))
        context['form']=CartForm()
        return context
    
    def post(self,request,*args,**kwargs):
        quantity=request.POST.get('quantity')
        user=request.user
        product=Products.objects.get(id=kwargs.get("id"))
        cart_obj=Cart.objects.filter(user=user,product=product).exclude(status="order-placed")
        print(cart_obj)
        if cart_obj:
            cart_data=cart_obj[0]
            cart_data.quantity+=int(quantity)
            cart_data.save()
            messages.success(request,'product added')
            return redirect("home_view")
        else:
            Cart.objects.create(user=user,product=product,quantity=quantity)
            messages.success(request,"Product added")
            return redirect('home_view')


@method_decorator(login_required,name='dispatch')
class CartListView(ListView):
    template_name="cartlist.html"
    model=Cart
    context_object_name="cart"

    def get_queryset(self):
         return Cart.objects.filter(user=self.request.user,status="in-cart")
   

class PlaceOrderView(TemplateView):
    template_name="place_order.html"

    def get_context_data(self,**kwargs):
        context=super().get_context_data(**kwargs)
        context['form']=OrderForm()
        context['product']=Cart.objects.get(id=kwargs.get("id"))
        return context
    
    def post(self,request,*args,**kwargs):
        address=request.POST.get("address")
        email=request.POST.get("email")
        user=request.user
        cart_obj=Cart.objects.get(id=kwargs.get("id"))
        Orders.objects.create(user=user,product=cart_obj,address=address,email=email)
        messages.success(request,"order placed successfully")
        cart_obj.status="order-placed"
        cart_obj.save()
        res=send_mail("Ekart","order placed successfully",settings.EMAIL_HOST_USER,[email])
        if res==1:
            return redirect('home_view')
        else:
            messages.warning(request,"somthing went wrong")
        return redirect('cartlist_view')
    

class OrderListView(ListView):
    template_name="orderlist.html"
    model=Orders
    context_object_name="orders"

    def get_queryset(self):
         return Orders.objects.filter(user=self.request.user,status="order-placed")