from edc_base.model_managers import HistoricalRecords
from edc_base.model_mixins import BaseUuidModel
from edc_visit_schedule.model_mixins import OnScheduleModelMixin, OnScheduleModelManager


class OnScheduleW10(OnScheduleModelMixin, BaseUuidModel):

    """A model used by the system. Auto-completed by the signal.
    """

    objects = OnScheduleModelManager()

    history = HistoricalRecords()
