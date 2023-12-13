from django.contrib import admin
from django.contrib.auth.models import User
from .models import Profile
from django.contrib.auth.admin import UserAdmin


class AccountInline(admin.StackedInline):
    model = Profile
    can_delete = False
    verbose_name_plural = 'Accounts'
    

class CustomiseUserAdmin (UserAdmin):
    inlines = (AccountInline,)
    
    
admin.site.unregister(User)
admin.site.register(User, CustomiseUserAdmin )
admin.site.register(Profile)



