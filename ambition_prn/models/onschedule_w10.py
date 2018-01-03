from django.contrib.sites.managers import CurrentSiteManager
from edc_base.model_managers import HistoricalRecords
from edc_base.model_mixins import BaseUuidModel
from edc_identifier.managers import SubjectIdentifierManager
from edc_visit_schedule.model_mixins import OnScheduleModelMixin


class OnScheduleW10(OnScheduleModelMixin, BaseUuidModel):

    """A model used by the system. Auto-completed by the signal.
    """

    objects = SubjectIdentifierManager()

    history = HistoricalRecords()

    on_site = CurrentSiteManager()
