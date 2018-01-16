from django.contrib.sites.managers import CurrentSiteManager
from django.db import models
from edc_base.model_managers import HistoricalRecords
from edc_base.model_mixins import BaseUuidModel
from edc_base.sites.site_model_mixin import SiteModelMixin


from .base_death_report_tmg import BaseDeathReportTmg


class DeathReportTmgManager(models.Manager):

    def get_by_natural_key(self, subject_identifier):
        return self.get(death_report__subject_identifier=subject_identifier)


class DeathReportTmgOne(BaseDeathReportTmg, SiteModelMixin, BaseUuidModel):

    on_site = CurrentSiteManager()

    objects = DeathReportTmgManager()

    history = HistoricalRecords()

    class Meta:
        verbose_name_plural = 'Death report TMG 1'


class DeathReportTmgTwo(BaseDeathReportTmg, SiteModelMixin, BaseUuidModel):

    on_site = CurrentSiteManager()

    objects = DeathReportTmgManager()

    history = HistoricalRecords()

    class Meta:
        verbose_name_plural = 'Death report TMG 2'
