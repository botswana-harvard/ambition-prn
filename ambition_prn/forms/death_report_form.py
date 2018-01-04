from django import forms
from edc_form_validators import FormValidatorMixin

from ..form_validators import DeathReportFormValidator
from ..models import DeathReport


class DeathReportForm(FormValidatorMixin, forms.ModelForm):

    form_validator_cls = DeathReportFormValidator

    subject_identifier = forms.CharField(
        label='Subject identifier',
        required=False,
        widget=forms.TextInput(attrs={'readonly': 'readonly'}))

    class Meta:
        model = DeathReport
        fields = '__all__'
