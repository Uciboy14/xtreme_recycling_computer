from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
	path('', views.index, name='index'),
	path('product/<str:id>/', views.product_details, name='product_details'),
    path('add_to_cart/', views.add_to_cart, name='add_to_cart'),
    path('categories/<str:id>/', views.category_products, name='category_products'),
    path('brands/<str:id>/', views.brand_products, name='brand_products'),
    path('contact/', views.contact_us, name='contact_us'),
    path('update-cart-item/', views.update_cart_item, name='update_cart_item'),
    path('remove-cart-item/', views.remove_cart, name='remove_cart'),
    path('cart/', views.cart, name='cart'),
    path('register/', views.register, name='register'),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),  # Use auth_views.LogoutView here
]