import pytz

from arrow.arrow import Arrow
from datetime import timedelta
from django.db.models.signals import post_save
from django.dispatch import receiver
from edc_constants.constants import YES, NO
from edc_visit_schedule.site_visit_schedules import site_visit_schedules

from .study_termination_conclusion import StudyTerminationConclusion


@receiver(post_save, weak=False, sender=StudyTerminationConclusion,
          dispatch_uid='study_termination_conclusion_on_post_save')
def study_termination_conclusion_on_post_save(sender, instance, raw, created, **kwargs):
    """Enroll to W10 if willing_to_complete_10w == YES.
    """
    if not raw:

        visit_schedule = site_visit_schedules.get_visit_schedule(
            visit_schedule_name='visit_schedule')
        schedule = visit_schedule.schedules.get('schedule')
        # convert date to UTC datetime
        offschedule_datetime = Arrow.fromdate(
            instance.last_study_fu_date + timedelta(days=1),
            pytz.utc).datetime - timedelta(seconds=1)
        schedule.take_off_schedule(
            subject_identifier=instance.subject_identifier,
            offschedule_datetime=offschedule_datetime)

        if instance.willing_to_complete_10w in [YES, NO]:
            onschedule = schedule.get_onschedule(
                subject_identifier=instance.subject_identifier)
            visit_schedule = site_visit_schedules.get_visit_schedule(
                'visit_schedule_w10')
            schedule_w10 = visit_schedule.schedules.get('schedule')
            if instance.willing_to_complete_10w == YES:
                schedule_w10.put_on_schedule(
                    subject_identifier=instance.subject_identifier,
                    consent_identifier=onschedule.consent_identifier)
            elif instance.willing_to_complete_10w == NO:
                schedule_w10.take_off_schedule(
                    subject_identifier=onschedule.consent_identifier)
