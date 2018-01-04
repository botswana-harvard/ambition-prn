from ambition_rando.tests.ambition_test_case_mixin import AmbitionTestCaseMixin
from django.test import TestCase, tag
from edc_action_item import create_action_item, SingletonActionItemError
from edc_action_item.models.action_item import ActionItem
from edc_constants.constants import CLOSED
from edc_facility.import_holidays import import_holidays
from edc_registration.models import RegisteredSubject
from model_mommy import mommy

from ..action_items import DeathReportAction


class TestDeathReport(AmbitionTestCaseMixin, TestCase):

    def setUp(self):
        import_holidays()
        self.subject_identifier = '12345'
        RegisteredSubject.objects.create(
            subject_identifier=self.subject_identifier)

    def test_add_action(self):
        create_action_item(
            action_cls=DeathReportAction,
            subject_identifier=self.subject_identifier)
        self.assertRaises(
            SingletonActionItemError,
            create_action_item,
            action_cls=DeathReportAction,
            subject_identifier=self.subject_identifier)

    def test_death_report_closes_action(self):
        create_action_item(
            action_cls=DeathReportAction,
            subject_identifier=self.subject_identifier)
        death_report = mommy.make_recipe(
            'ambition_prn.deathreport',
            subject_identifier=self.subject_identifier)
        obj = ActionItem.objects.get(
            action_identifier=death_report.action_identifier)
        self.assertEqual(obj.status, CLOSED)
