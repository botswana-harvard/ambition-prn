from django import forms

from edc_base.sites.forms import SiteModelFormMixin

from ..form_validators import DeathReportFormValidator
from ..models import DeathReportTmgOne, DeathReportTmgTwo


class DeathReportTmgOneForm(SiteModelFormMixin, forms.ModelForm):

    form_validator_cls = DeathReportFormValidator

    class Meta:
        model = DeathReportTmgOne
        fields = '__all__'


class DeathReportTmgTwoForm(SiteModelFormMixin, forms.ModelForm):

    form_validator_cls = DeathReportFormValidator

    class Meta:
        model = DeathReportTmgTwo
        fields = '__all__'
