from django.urls import path

from .views import (
    productlistview,
    productdetailview,
    productdeleteview, 
    productcreateview,
    productupdateview
    )

app_name = "product"
urlpatterns = [
    path("", view=productlistview, name="product_list"),
    path("<int:pk>/", view=productdetailview, name="product_detail"),
    path("<int:pk>/delete/", view=productdeleteview, name="product_delete"),
    path("create/", view=productcreateview, name="product_create"),
    path("<int:pk>/update/", view=productupdateview, name="product_update"),

]
