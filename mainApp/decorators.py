from mainApp.models import SellerAccount
from django.http import HttpResponseRedirect
from django.http.response import HttpResponse, HttpResponse
from django.shortcuts import redirect
from django.urls import reverse


def has_selleraccount(view_func):
    def wrap(request, *args, **kwargs):
        user = request.user
        print(str(user.username))
        try:
            if request.user.selleraccount.profile_complete == False:
                # return redirect("extended-user")
                return view_func(request, *args, **kwargs)
                
            else:
                return HttpResponseRedirect(reverse("extended-user"))
                
        except:
            return HttpResponseRedirect(reverse("extended-user"))
    return wrap