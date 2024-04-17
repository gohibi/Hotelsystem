from django.urls import path
from hotel.views import index , detail_hotel

app_name="hotel"

urlpatterns = [
    path('',index,name="index"),
    path('details-hotel/<slug>',detail_hotel , name="details-hotel"),

]