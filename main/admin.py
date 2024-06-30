from django.contrib import admin
from.models import Table, MenuItem, Booking

class TableAdmin(admin.ModelAdmin):
    list_display = ('table_number', 'seats','available')
    search_fields = ('table_number',)

class MenuItemAdmin(admin.ModelAdmin):
    list_display = ('name', 'price')
    search_fields = ('name',)

class BookingAdmin(admin.ModelAdmin):
    list_display = ('user', 'table', 'booking_time', 'number_of_people')
    search_fields = ('user__username', 'table__table_number')
    list_filter = ('booking_time',)

admin.site.register(Table, TableAdmin)
admin.site.register(MenuItem, MenuItemAdmin)
admin.site.register(Booking, BookingAdmin)