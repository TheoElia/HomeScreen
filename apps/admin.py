from django.contrib import admin
from .models import *
from .forms import *


class AppImageInline(admin.TabularInline):
    model = AppImage  # readonly_fields = ['image_tag',]
    extra = 3

    def image_tag(self, obj):

        return mark_safe('<img src="{url}" width="{width}" height={height} "/>'.format(
            url = obj.image.url,
            width = 100,#obj.img.width,
            height=100,))#obj.img.height,))
    image_tag.short_description = 'Image'


class AppAdmin(admin.ModelAdmin):
    add_form = AppCreationForm
    form = AppChangeForm
    model = App
    ## Defines the list of fields displayed on admin page
    list_display = ['name','owner']
    # actions = my_actions
    inlines = [ AppImageInline, ]

    def get_queryset(self, request):
        if request.user.is_superuser:
            return App.objects.all()
        if request.user.is_staff:
            return App.objects.filter(owner=request.user)
        # if is_member(request.user.id,"Administrators"):
        #     return Pharmacy.objects.all()
        return None




# Register your models here.
admin.site.register(App,AppAdmin)
admin.site.register(Category)
admin.site.register(Rate)
