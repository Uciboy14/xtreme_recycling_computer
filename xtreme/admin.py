from django.contrib import admin
from .models import Product
from .models import Brand
from .models import Category
from .models import Order
from .models import Payment
from .models import Cart
from .models import CartItem

# Register your models here.
admin.site.register(Product)
admin.site.register(Brand)
admin.site.register(Category)
admin.site.register(Order)
admin.site.register(Payment)
admin.site.register(Cart)
admin.site.register(CartItem)



