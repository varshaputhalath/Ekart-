from django.urls import path
from AdminApp import views


urlpatterns=[
    path('new_order_list',views.NewOrderList.as_view(),name="new_order_list"),
    path('confirm_order/<int:id>',views.OrderConfirmView.as_view(),name="confirm_order_view"),
    path('all_order_list',views.AllOrdersView.as_view(),name="all_order_list"),
    path('order_detail/<int:id>',views.OrderDetailView.as_view(),name="order_detail_view"),
    
]