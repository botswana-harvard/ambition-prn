from django import forms
from edc_form_validators import FormValidatorMixin

from ..form_validators import ProtocolDeviationViolationFormValidator
from ..models import ProtocolDeviationViolation


class ProtocolDeviationViolationForm(FormValidatorMixin, forms.ModelForm):

    form_validator_cls = ProtocolDeviationViolationFormValidator

    class Meta:
        model = ProtocolDeviationViolation
        fields = '__all__'
