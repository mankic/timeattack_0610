from django.contrib import admin
from .models import Category,Product,OrderStatus,UserOrder,ProductOrder

# Register your models here.
admin.site.register(Category)
admin.site.register(Product)
admin.site.register(OrderStatus)
admin.site.register(UserOrder)
admin.site.register(ProductOrder)
