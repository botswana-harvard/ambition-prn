from django.contrib import admin

from ..admin_site import ambition_prn_admin
from ..models import Enrollment
from .modeladmin_mixins import ModelAdminMixin


@admin.register(Enrollment, site=ambition_prn_admin)
class EnrollmentAdmin(ModelAdminMixin, admin.ModelAdmin):

    instructions = None
    fields = (
        'subject_identifier', 'report_datetime', 'consent_identifier')

    def get_readonly_fields(self, request, obj=None):
        return ('subject_identifier', 'report_datetime', 'consent_identifier')
