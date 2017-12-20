from edc_appointment.model_mixins import CreateAppointmentsMixin
from edc_base.model_managers import HistoricalRecords
from edc_base.model_mixins import BaseUuidModel
from edc_visit_schedule.model_mixins import OnScheduleModelMixin, OnScheduleModelManager


class OnScheduleW10(OnScheduleModelMixin, CreateAppointmentsMixin,
                    BaseUuidModel):

    """A model used by the system. Auto-completed by the signal.
    """

    ADMIN_SITE_NAME = 'ambition_prn_admin'

    objects = OnScheduleModelManager()

    history = HistoricalRecords()

    class Meta(OnScheduleModelMixin.Meta):
        consent_model = 'ambition_subject.subjectconsent'
        visit_schedule_name = 'visit_schedule_w10.schedule'
