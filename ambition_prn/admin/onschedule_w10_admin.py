from django.contrib import admin

from ..admin_site import ambition_prn_admin
from ..models import OnScheduleW10
from .modeladmin_mixins import ModelAdminMixin


@admin.register(OnScheduleW10, site=ambition_prn_admin)
class OnScheduleW10Admin(ModelAdminMixin, admin.ModelAdmin):

    instructions = None
    fields = (
        'subject_identifier', 'onschedule_datetime')

    list_display = ('subject_identifier', 'dashboard', 'onschedule_datetime')

    list_filter = ('onschedule_datetime', )

    def get_readonly_fields(self, request, obj=None):
        return ('subject_identifier', 'onschedule_datetime')
