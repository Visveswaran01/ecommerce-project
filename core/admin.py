from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .forms import CustomUserCreationForm
from .models import *

class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    model = Consumer
    list_display = ('username', 'fname', 'lname', 'is_staff', 'date_joined')
    search_fields = ('username','fname', 'lname')
    ordering = ('fname', 'lname')

admin.site.register(Consumer, CustomUserAdmin)






