from django.contrib.sites.managers import CurrentSiteManager
from django.db import models
from edc_action_item.model_mixins import ActionItemModelMixin
from edc_base.model_managers import HistoricalRecords
from edc_base.model_mixins import BaseUuidModel
from edc_base.model_validators import date_not_future
from edc_base.utils import get_utcnow
from edc_identifier.model_mixins import TrackingIdentifierModelMixin
from edc_visit_schedule.model_mixins import OffScheduleModelMixin, OffScheduleModelManager

from ..action_items import StudyTerminationConclusionW10Action
from ..choices import REASON_STUDY_TERMINATED


class StudyTerminationConclusionW10(OffScheduleModelMixin, ActionItemModelMixin,
                                    TrackingIdentifierModelMixin, BaseUuidModel):

    action_cls = StudyTerminationConclusionW10Action
    tracking_identifier_prefix = 'ST'

    report_datetime = models.DateTimeField(
        verbose_name="Report Date and Time",
        default=get_utcnow)

    last_study_fu_date = models.DateField(
        verbose_name='Date of last research follow up (if different):',
        validators=[date_not_future],
        blank=True,
        null=True)

    termination_reason = models.CharField(
        verbose_name='Reason for study termination',
        max_length=75,
        choices=REASON_STUDY_TERMINATED,
        help_text=(
            'If included in error, be sure to fill in protocol deviation form.'))

    death_date = models.DateField(
        verbose_name='Date of Death',
        validators=[date_not_future],
        blank=True,
        null=True)

    consent_withdrawal_reason = models.CharField(
        verbose_name='Reason for withdrawing consent',
        max_length=75,
        blank=True,
        null=True)

    objects = OffScheduleModelManager()

    history = HistoricalRecords()

    on_site = CurrentSiteManager()

    def save(self, *args, **kwargs):
        self.offschedule_datetime = self.report_datetime
        super().save(*args, **kwargs)

    class Meta:
        verbose_name = 'W10 Study Termination/Conclusion'
        verbose_name_plural = 'W10 Study Terminations/Conclusions'
