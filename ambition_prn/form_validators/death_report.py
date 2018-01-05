from edc_constants.constants import OTHER
from edc_form_validators import FormValidator

from ..constants import TUBERCULOSIS
from .study_day_form_validator_mixin import StudyDayFormValidatorMixin


class DeathReportFormValidator(StudyDayFormValidatorMixin, FormValidator):

    def clean(self):

        self.validate_study_day_with_datetime(
            study_day=self.cleaned_data.get('study_day'),
            compare_datetime=self.cleaned_data.get('death_datetime'),
            study_day_field='study_day')

        self.validate_other_specify(
            field='cause_of_death',
            other_specify_field='cause_of_death_other',
            other_stored_value=OTHER)

        self.required_if(
            TUBERCULOSIS,
            field='cause_of_death',
            field_required='tb_site')
