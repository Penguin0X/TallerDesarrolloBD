from django.contrib import admin
from RegistroUser.models import User

# Register your models here.

class RegistroUserAdmin(admin.ModelAdmin):
    list_display = [field.name for field in User._meta.fields]

admin.site.register(User, RegistroUserAdmin)