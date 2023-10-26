from django.contrib import admin
from django.utils.translation import gettext_lazy as _


# Register your models here.
from.models import doctors,departments,appointments
admin.site.register(doctors)
admin.site.register(departments)
class AppointmentAdmin(admin.ModelAdmin):
     list_display = ('id', 'p_name', 'p_phone', 'p_email', 'get_doctor_name','p_msg','p_date')
admin.site.register(appointments,AppointmentAdmin)

_