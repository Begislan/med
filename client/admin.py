from django.contrib import admin
from .models import *

# Register your models here.
class RegionAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}

class DoctorAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}
    list_display = ['name', 'first_name', 'phone', 'department']

class DepartamentAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}

admin.site.register(Region, RegionAdmin)
admin.site.register(Doctor, DoctorAdmin)
admin.site.register(Client)
admin.site.register(Departament, DepartamentAdmin)


admin.site.register(Post)
admin.site.register(Diognoz)
admin.site.register(History)
