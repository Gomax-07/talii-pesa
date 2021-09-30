from django.contrib import admin
from .models import *


# Register your models here.

# Register the Admin classes for House using the decorator


# Register the Admin classes for rent using the decorator
@admin.register(Rent)
class RentAdmin(admin.ModelAdmin):
    list_filter = ('status', 'payment_date')

    fieldsets = (
        (None, {
            'fields': ('house', 'amount', 'id')
        }),
        ('Pending', {
            'fields': ('status', 'payment_date')
        }),
    )


class RentInline(admin.TabularInline):
    model = Rent


@admin.register(House)
class HouseAdmin(admin.ModelAdmin):
    list_display = ('house_name', 'tenant', 'display_caretaker')

    inlines = [RentInline]


admin.site.register(Caretaker)


# admin.site.register(Tenant)
# Define the admin class
class TenantAdmin(admin.ModelAdmin):
    list_display = ('last_name', 'first_name', 'date_of_birth', 'date_of_entry')

    fields = ['first_name', 'last_name', ('date_of_birth', 'date_of_entry')]


admin.site.register(Tenant, TenantAdmin)
