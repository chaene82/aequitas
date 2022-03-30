from django.contrib import admin

# Register your models here.
from .models import Profile
from django.contrib.auth.models import User, Group


#admin.site.register(Profile)


class ProfileInline(admin.StackedInline):
    model = Profile

class UserAdmin(admin.ModelAdmin):
    model = User
    fields = ["username"]
    inlines = [ProfileInline]

admin.site.unregister(User)
admin.site.register(User, UserAdmin)
admin.site.unregister(Group)    