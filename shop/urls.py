from django.urls import path
from . import views
app_name='shop'
urlpatterns = [
    path('',views.allProductcat,name='allProductcat'),
    path('<slug:c_slug>/',views.allProductcat,name='products_by_category'),
    path('<slug:c_slug>/<slug:product_slug>',views.proDetail,name='productCatdetail')
]