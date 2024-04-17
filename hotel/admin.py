from django.contrib import admin
from hotel.models import (
    Hotel,HotelGallery,HotelFeatures,HotelFaq,RoomType,Room ,
    Booking ,ActivityLog,StaffOnDuty
                        )
# Register your models here.
class HoteLGalleryInline(admin.TabularInline):
    model = HotelGallery

class HotelAdmin(admin.ModelAdmin):
    inlines = [HoteLGalleryInline]
    list_display = ['thumbnail','name','user','status']
    prepopulated_fields = {
        'slug': ('name',)
    }

admin.site.register(Hotel, HotelAdmin)
admin.site.register(Booking)
admin.site.register(RoomType)
admin.site.register(Room)
admin.site.register(ActivityLog)
admin.site.register(StaffOnDuty)

