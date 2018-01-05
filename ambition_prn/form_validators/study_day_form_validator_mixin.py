import pytz

from arrow.arrow import Arrow
from django import forms
from django.conf import settings
from edc_base.utils import convert_php_dateformat
from edc_form_validators.base_form_validator import INVALID_ERROR
from edc_registration.models import RegisteredSubject


class StudyDayFormValidatorMixin:

    def validate_study_day_with_datetime(self, study_day=None,
                                         compare_datetime=None,
                                         study_day_field=None):
        """Raises an exception if study day does not match
        calculation against import pytz.

        Note: study-day is 1-based.
        """
        if study_day is not None:
            if compare_datetime:
                randomization_datetime = RegisteredSubject.objects.get(
                    subject_identifier=self.cleaned_data.get(
                        'subject_identifier')).randomization_datetime
                days_on_study = (
                    compare_datetime.date() - randomization_datetime.date()).days
                if study_day - 1 != days_on_study:
                    tz = pytz.timezone(settings.TIME_ZONE)
                    formatted_date = Arrow.fromdatetime(
                        randomization_datetime).to(tz).strftime(
                            convert_php_dateformat(settings.DATETIME_FORMAT))
                    message = {
                        study_day_field: (
                            f'Invalid. Expected {days_on_study + 1}. '
                            f'Subject was registered on {formatted_date}')}
                    self._errors.update(message)
                    self._error_codes.append(INVALID_ERROR)
                    raise forms.ValidationError(message, code=INVALID_ERROR)
