from django.urls import path
from hotel.views import index , detail_hotel , room_type_detail

app_name="hotel"

urlpatterns = [
    path('',index,name="index"),
    path('details-hotel/<slug>',detail_hotel , name="details-hotel"),
    path('detail/<slug:slug>/room-type=<slug:rt_slug>', room_type_detail , name="room-type-detail")

]