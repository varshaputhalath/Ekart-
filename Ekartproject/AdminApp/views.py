from django.shortcuts import render,redirect
from django.views.generic import ListView,DetailView
from UserApp.models import Orders
from django.views import View
from django.core.mail import send_mail,settings
from django.contrib import messages 
from AdminApp.forms import OrderUpdateForm
from django.contrib.auth.models import User

# Create your views here.
class NewOrderList(ListView):
    template_name='dashboard.html'
    model=Orders
    context_object_name="orders"

    def get_queryset(self):
        return Orders.objects.filter(status="order-placed")
    
class OrderConfirmView(View):
    def get(self,request,*args,**kwargs):
        order=Orders.objects.get(id=kwargs.get("id"))
        to=order.email
        send_mail("Ekart","order confirmed!",settings.EMAIL_HOST_USER,[to])
        messages.success(request,"Order Confirmed")
        return redirect('new_order_list')
    
class AllOrdersView(ListView):
    template_name="all_orders.html"
    model=Orders
    context_object_name="orders"

    def get_queryset(self):
        return Orders.objects.all().exclude(status="delivered")

class OrderDetailView(DetailView):
    template_name='order_detail.html'
    model=Orders
    context_object_name="order"
    pk_url_kwarg="id"

    def get_context_data(self, **kwargs):
        context=super().get_context_data(**kwargs)
        context['form']=OrderUpdateForm()
        return context
    
    def post(self,request,*args,**kwargs):
        status=request.POST.get('status')
        exp_date=request.POST.get('exp_date')
        order=Orders.objects.get(id=kwargs.get('id'))
        order.status=status
        order.exp_date=exp_date
        order.save()
        # user=User.objects.get(id=order.user_id)
        # to=user.email
        to=order.email
        res=send_mail("Ekart",f"Expected delivery date: {exp_date}",settings.EMAIL_HOST_USER,[to])
        print(res)
        return redirect('all_order_list')