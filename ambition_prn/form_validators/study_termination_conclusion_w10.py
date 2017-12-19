from django import forms
from django.apps import apps as django_apps
from django.core.exceptions import ObjectDoesNotExist
from edc_form_validators import FormValidator
from edc_constants.constants import DEAD

from ..constants import CONSENT_WITHDRAWAL


class StudyTerminationConclusionW10FormValidator(FormValidator):

    death_report_model = 'ambition_prn.deathreport'

    @property
    def death_report_model_cls(self):
        return django_apps.get_model(self.death_report_model)

    def clean(self):

        if self.cleaned_data.get('termination_reason') == DEAD:
            try:
                self.death_report_model_cls.objects.get(
                    subject_identifier=self.cleaned_data.get('subject_identifier'))
            except ObjectDoesNotExist:
                raise forms.ValidationError({
                    'termination_reason':
                    'Patient is deceased, please complete death form first.'})

        self.required_if(
            DEAD,
            field='termination_reason',
            field_required='death_date')

        self.required_if(
            CONSENT_WITHDRAWAL,
            field='termination_reason',
            field_required='consent_withdrawal_reason')

        self.applicable_if(
            CONSENT_WITHDRAWAL,
            field='termination_reason',
            field_applicable='willing_to_complete_10w')

        self.applicable_if(
            'care_transferred_to_another_institution',
            field='termination_reason',
            field_applicable='willing_to_complete_centre')
