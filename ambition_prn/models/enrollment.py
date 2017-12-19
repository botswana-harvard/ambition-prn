from django.db import models
from edc_appointment.model_mixins import CreateAppointmentsMixin
from edc_base.model_managers import HistoricalRecords
from edc_base.model_mixins import BaseUuidModel
from edc_visit_schedule.model_mixins import EnrollmentModelMixin


class EnrollmentManager(models.Manager):

    def get_by_natural_key(self, subject_identifier,
                           visit_schedule_name, schedule_name):
        return self.get(
            subject_identifier=subject_identifier,
            visit_schedule_name=visit_schedule_name,
            schedule_name=schedule_name)


class Enrollment(EnrollmentModelMixin, CreateAppointmentsMixin,
                 BaseUuidModel):

    """A model used by the system. Auto-completed by subject_consent.
    """

    ADMIN_SITE_NAME = 'ambition_prn_admin'

    objects = EnrollmentManager()

    history = HistoricalRecords()

    class Meta(EnrollmentModelMixin.Meta):
        consent_model = 'ambition_subject.subjectconsent'
        visit_schedule_name = 'visit_schedule.schedule'
