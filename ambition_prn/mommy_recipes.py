from edc_constants.constants import YES
from faker import Faker
from model_mommy.recipe import Recipe

from .models import DeathReport, StudyTerminationConclusion, StudyTerminationConclusionW10
from .models import ProtocolDeviationViolation

fake = Faker()

deathreport = Recipe(
    DeathReport,
    study_day=1,
    death_as_inpatient=YES,
    cause_of_death_study_doctor_opinion='art_toxicity',
    cause_other_study_doctor_opinion='None',
    cause_tb_study_doctor_opinion=None,
    cause_of_death_tmg1_opinion='art_toxicity',
    cause_other_tmg1_opinion='None',
    cause_tb_tmg1_opinion=None,
    cause_of_death_tmg2_opinion='art_toxicity',
    cause_other_tmg2_opinion='None',
    cause_tb_tmg2_opinion=None,
    narrative_summary=(
        'adverse event resulted in death due to cryptococcal meningitis'))

studyterminationconclusion = Recipe(StudyTerminationConclusion)

studyterminationconclusionw10 = Recipe(StudyTerminationConclusionW10)

protocoldeviationviolation = Recipe(ProtocolDeviationViolation)
