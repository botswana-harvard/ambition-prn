from django.contrib import admin

from ..admin_site import ambition_prn_admin
from ..models import OffSchedule
from .modeladmin_mixins import ModelAdminMixin


@admin.register(OffSchedule, site=ambition_prn_admin)
class OffScheduleAdmin(ModelAdminMixin, admin.ModelAdmin):

    instructions = None
    fields = (
        'subject_identifier', 'offschedule_datetime', 'consent_identifier')

    list_display = ('subject_identifier',
                    'offschedule_datetime', 'consent_identifier')

    list_filter = ('offschedule_datetime', )

    def get_readonly_fields(self, request, obj=None):
        return ('subject_identifier', 'offschedule_datetime', 'consent_identifier')
