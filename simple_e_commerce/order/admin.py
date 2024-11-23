from django.contrib import admin

from simple_e_commerce.order.models import Order, OrderItem

# Register your models here.
@admin.register(Order) 
class OrderAdmin(admin.ModelAdmin):
    list_display = ["id", "user", "total", "status", "created_at"]
    list_filter = ["status", "created_at"]
    search_fields = ["user__username"]

@admin.register(OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
    list_display = ["order", "product", "quantity", "price"]
    search_fields = ["order__id", "product__name"]