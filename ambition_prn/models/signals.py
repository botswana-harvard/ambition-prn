from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from edc_constants.constants import YES
from edc_visit_schedule import EnrollToSchedule

from .study_termination_conclusion import StudyTerminationConclusion
from .study_termination_conclusion_w10 import StudyTerminationConclusionW10

post_delete.providing_args = set(["instance", "using", "raw"])

enrollment_model = 'ambition_prn.enrollment'
enrollment_model_w10 = 'ambition_prn.enrollmentw10'


@receiver(post_save, weak=False, sender=StudyTerminationConclusion,
          dispatch_uid='study_termination_conclusion_on_post_save')
def study_termination_conclusion_on_post_save(sender, instance, raw, created, **kwargs):
    if not raw:
        if not created:
            enroll = EnrollToSchedule(enrollment_model=enrollment_model)
            enroll.update(subject_identifier=instance.subject_identifier)
        else:
            if instance.willing_to_complete_10w == YES:
                enroll = EnrollToSchedule(
                    enrollment_model=enrollment_model_w10)
                enroll.enroll(
                    subject_identifier=instance.subject_identifier,
                    consent_identifier=None,
                    is_eligible=True)


@receiver(post_delete, weak=False, sender=StudyTerminationConclusion,
          dispatch_uid="study_termination_conclusion_on_post_delete")
def study_termination_conclusion_on_post_delete(sender, instance, raw, using, **kwargs):
    if not raw:
        enroll = EnrollToSchedule(enrollment_model=enrollment_model)
        enroll.update(subject_identifier=instance.subject_identifier)


@receiver(post_delete, weak=False, sender=StudyTerminationConclusionW10,
          dispatch_uid="study_termination_conclusion_w10_on_post_delete")
def study_termination_conclusion_w10_on_post_delete(sender, instance, raw, using, **kwargs):
    if not raw:
        enroll = EnrollToSchedule(enrollment_model=enrollment_model_w10)
        enroll.update(subject_identifier=instance.subject_identifier)
