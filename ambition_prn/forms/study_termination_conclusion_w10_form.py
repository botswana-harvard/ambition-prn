from django import forms
from edc_offstudy.modelform_mixins import OffstudyModelFormMixin

from ..models import StudyTerminationConclusionW10
from ..form_validators import StudyTerminationConclusionW10FormValidator


class StudyTerminationConclusionW10Form(OffstudyModelFormMixin, forms.ModelForm):

    form_validator_cls = StudyTerminationConclusionW10FormValidator

    class Meta:
        model = StudyTerminationConclusionW10
        fields = '__all__'
        labels = {
            'offstudy_datetime': 'Date patient terminated on study:',
        }
