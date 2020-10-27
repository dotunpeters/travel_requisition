from django.contrib import admin
from .models import User, Travel

# Register your models here.


class TravelAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['trip', 'traveldate', 'staff']}),
        ('Approval', {'fields': ['status']}),
    ]
    readonly_fields = ['trip', 'traveldate', 'staff']

    list_display = ('staff', 'trip', 'traveldate', 'status')

    def has_add_permission(self, request, obj=None):
        return False


admin.site.register(Travel, TravelAdmin)
