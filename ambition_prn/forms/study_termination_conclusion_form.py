from django import forms
from edc_form_validators import FormValidatorMixin

from ..form_validators import StudyTerminationConclusionFormValidator
from ..models import StudyTerminationConclusion


class StudyTerminationConclusionForm(FormValidatorMixin, forms.ModelForm):

    form_validator_cls = StudyTerminationConclusionFormValidator

    class Meta:
        model = StudyTerminationConclusion
        fields = '__all__'
        labels = {
            'offschedule_datetime': 'Date patient terminated on study:',
        }
