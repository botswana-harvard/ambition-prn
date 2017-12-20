from edc_base.model_managers import HistoricalRecords
from edc_base.model_mixins import BaseUuidModel
from edc_consent.model_mixins import RequiresConsentModelMixin
from edc_visit_schedule.model_mixins import OffScheduleModelMixin, OffScheduleModelManager


class OffSchedule(OffScheduleModelMixin, RequiresConsentModelMixin,
                  BaseUuidModel):

    ADMIN_SITE_NAME = 'ambition_prn_admin'

    objects = OffScheduleModelManager()

    history = HistoricalRecords()

    class Meta(OffScheduleModelMixin.Meta):
        visit_schedule_name = 'visit_schedule.schedule'
        consent_model = 'ambition_subject.subjectconsent'
