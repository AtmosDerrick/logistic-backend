from django.contrib import admin
from django.contrib.auth.models import Group,User
from .models import Profile


# #Unregister Group
# admin.site.unregister(Group)

# #Mix Profile info into User info
# class ProfileIninline(admin.StackedInline):
#     model =Profile

# #Extend User Model
# class UserAdmin(admin.ModelAdmin):
#     model = User
    # inlines = [ProfileIninline]

# # Register your models here.

# #unregister initial User
admin.site.register(Profile)

# #Register User


