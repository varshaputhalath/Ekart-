from django.urls import path
from UserApp import views


urlpatterns=[
    path('',views.Home.as_view(),name="home_view"),
    path('signup',views.SignUpView.as_view(),name="signup_view"),
    path('signin',views.SignInView.as_view(),name="signin_view"),
    path('signout',views.SignoutView.as_view(),name="signout_view"),
    path('product_detail/<int:id>',views.ProductDetailView.as_view(),name="productdetail_view"),
    path('addtocart/<int:id>',views.AddToCartView.as_view(),name="addtocart_view"),
    path('cartlist',views.CartListView.as_view(),name="cartlist_view"),
    path('place_order/<int:id>',views.PlaceOrderView.as_view(),name="placeorder_view"),
    path('order_list',views.OrderListView.as_view(),name="orderlist_view"),

   

]