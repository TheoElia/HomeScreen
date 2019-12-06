from django.contrib import admin
from .models import *
from .forms import *
from django.contrib.auth.admin import UserAdmin


class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    # Defines the list of fields displayed on admin page
    list_display = ['username','email', 'date_joined',]
    # fields = ['username','email',  'password', 'date_joined','is_active','is_staff','address']
    # readonly_fields = ['image_tag',]
    # Enables editing other fields

    fieldsets = UserAdmin.fieldsets + (
      ('Extra Fields', {'fields': ('user_img',)}),
    )
    # actions = [make_staff,add_to_students]

    def get_queryset(self, request):
        if request.user.is_superuser:
            return CustomUser.objects.all()
        # if self.is_member(request.user.id, 'Patrons'):
            #print(Retailer.objects.filter(admin=request.user.id))
            # return Patron.objects.filter(id=request.user.id)
        return None

# Register your models here.
admin.site.register(CustomUser,CustomUserAdmin)