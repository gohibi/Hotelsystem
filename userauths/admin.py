from django.contrib import admin
from userauths.models import Profile,User
# Register your models here.
class UserAdmin(admin.ModelAdmin):
    search_fields = ['full_name','username']
    list_display = ['full_name','username','email','gender','phone']

class ProfileAdmin(admin.ModelAdmin):
    search_fields = ['full_name','user__username']
    list_display = ['full_name','user','verified']

admin.site.register(Profile,ProfileAdmin)
admin.site.register(User,UserAdmin)