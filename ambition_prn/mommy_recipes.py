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
    cause_of_death='art_toxicity',
    cause_of_death_other=None,
    tb_site='meningitis',
    death_narrative=(
        'adverse event resulted in death due to cryptococcal meningitis'))

studyterminationconclusion = Recipe(StudyTerminationConclusion)

studyterminationconclusionw10 = Recipe(StudyTerminationConclusionW10)

protocoldeviationviolation = Recipe(ProtocolDeviationViolation)
