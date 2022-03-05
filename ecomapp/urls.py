from django.urls import path
from .views import ContactusView, HomeView, AboutView, AllProductsView, ProductDetailView
app_name = "ecomapp"
urlpatterns = [ 
    path("",HomeView.as_view(),name="home"),
    path("about/",AboutView.as_view(),name="about"),
    path("contactus/", ContactusView.as_view(),name="contactus"),    
    path('all-products/', AllProductsView.as_view(), name="allproducts"), 
    path("product/<slug:slug>/", ProductDetailView.as_view(), name="productdetail"),
]

    