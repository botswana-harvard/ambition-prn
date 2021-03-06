from django.contrib import admin
from edc_action_item import action_fieldset
from edc_model_admin import audit_fieldset_tuple

from ..admin_site import ambition_prn_admin
from ..forms import DeathReportTmgForm
from ..models import DeathReportTmg, DeathReport
from .modeladmin_mixins import ModelAdminMixin


@admin.register(DeathReportTmg, site=ambition_prn_admin)
class DeathReportTmgAdmin(ModelAdminMixin, admin.ModelAdmin):

    form = DeathReportTmgForm

    fieldsets = (
        (None, {
            'fields': (
                'subject_identifier',
                'death_report',
                'report_datetime')}),
        ('Opinion of TMG', {
            'fields': (
                'cause_of_death',
                'cause_of_death_other',
                'tb_site',
                'cause_of_death_agreed',
                'narrative',
                'report_status',
                'report_closed_datetime')}),
        action_fieldset,
        audit_fieldset_tuple)

    radio_fields = {
        'cause_of_death': admin.VERTICAL,
        'cause_of_death_agreed': admin.VERTICAL,
        'tb_site': admin.VERTICAL,
        'report_status': admin.VERTICAL}

    list_display = ['subject_identifier', 'dashboard', 'report_datetime', 'cause_of_death',
                    'cause_of_death_agreed', 'status', 'report_closed_datetime']

    list_filter = ('report_datetime', 'report_status',
                   'cause_of_death_agreed', 'cause_of_death')

    search_fields = ['action_identifier',
                     'tracking_identifier', 'subject_identifier',
                     'death_report__action_identifier',
                     'death_report__tracking_identifier']

    def get_readonly_fields(self, request, obj=None):
        fields = super().get_readonly_fields(request, obj)
        fields = ('tracking_identifier', 'action_identifier') + fields
        if obj:
            fields = fields + ('subject_identifier', 'death_report')
        return fields

    def status(self, obj=None):
        return obj.report_status.title()

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == 'death_report':
            if request.GET.get('death_report'):
                kwargs["queryset"] = DeathReport.objects.filter(
                    id__exact=request.GET.get('death_report', 0))
            else:
                kwargs["queryset"] = DeathReport.objects.none()
        return super().formfield_for_foreignkey(db_field, request, **kwargs)
