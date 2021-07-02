from django.contrib import admin
from app_bem.models import (
    BEM,
    BEMDepartement,
    BEMUser,
    DepartmentScope
)


# Register your models here.


class BEMAdmin(admin.ModelAdmin):
    list_display = (
        'year',
        'start_period',
        'end_period',
    )


class BEMDepartementAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'head',
        'staff_amount',
        'bem',
    )


class BEMUserAdmin(admin.ModelAdmin):
    list_display = (
        'user',
        'department',
        'role',
    )


admin.site.register(BEM, BEMAdmin)
admin.site.register(BEMDepartement, BEMDepartementAdmin)
admin.site.register(BEMUser, BEMUserAdmin)
admin.site.register(DepartmentScope)
