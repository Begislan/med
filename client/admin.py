from django.contrib import admin
from .models import Post, Region, Doctor, Client

# Register your models here.
class RegionAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}

class DoctorAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}

admin.site.register(Region, RegionAdmin)
admin.site.register(Doctor, DoctorAdmin)
admin.site.register(Client)


admin.site.register(Post)
