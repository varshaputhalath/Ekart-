from django.contrib import messages
from django.shortcuts import redirect

def login_required(fn):
    def wrapper(request,*args,**kwargs):
        if not request.user.is_authenticated:
            messages.warning(request,"You must login first")
            return redirect("signin_view")
        else:
            return fn(request,*args,**kwargs)
    return wrapper