from django.contrib import admin

from ..admin_site import ambition_prn_admin
from ..models import EnrollmentW10
from .modeladmin_mixins import ModelAdminMixin


@admin.register(EnrollmentW10, site=ambition_prn_admin)
class EnrollmentW10Admin(ModelAdminMixin, admin.ModelAdmin):

    instructions = None
    fields = (
        'subject_identifier', 'report_datetime', 'consent_identifier')

    def get_readonly_fields(self, request, obj=None):
        return ('subject_identifier', 'report_datetime', 'consent_identifier')
