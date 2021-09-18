from django.urls import path, include
from AdminPanel import views


urlpatterns = [
    path('', views.get_adminpanel_url, name="AdminHome"),

    # Order Details URL
    path("order_details/<int:id>/", views.order_details, name="order_details"),

    path("uploaded-offer/", views.uploadedOfferView, name="uploaded-offer"),
    path("all-users/", views.allUsersView, name="all-users"),
    path("all-orders/", views.allOrdersView, name="all-orders"),
    path("admin-login/", views.adminLoginView, name="admin-login"),
    path("transaction/", views.transactionView, name="TransactionView"),

    # path(),
    
]