from django.contrib import admin
from hotel.models import (
    Hotel,HotelGallery,HotelFeatures,HotelFaq,RoomType,Room ,
    Booking ,ActivityLog,StaffOnDuty
                        )
# Register your models here.

class HotelAdmin(admin.ModelAdmin):
    list_display = ['thumbnail','name','user','status']
    prepopulated_fields = {
        'slug': ('name',)
    }

admin.site.register(Hotel, HotelAdmin)
admin.site.register(Booking)

