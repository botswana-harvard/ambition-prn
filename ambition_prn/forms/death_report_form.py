from django import forms
from edc_base.sites.forms import SiteModelFormMixin
from edc_form_validators import FormValidatorMixin

from ..form_validators import DeathReportFormValidator
from ..models import DeathReport


class DeathReportForm(SiteModelFormMixin, FormValidatorMixin, forms.ModelForm):

    form_validator_cls = DeathReportFormValidator

    subject_identifier = forms.CharField(
        label='Subject identifier',
        required=False,
        widget=forms.TextInput(attrs={'readonly': 'readonly'}))

    class Meta:
        model = DeathReport
        fields = '__all__'
