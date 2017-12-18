from edc_action_item import Action, HIGH_PRIORITY, site_action_items


PROTOCOL_DEVIATION_VIOLATION_ACTION = 'submit-protocol-deviation-violation'
STUDY_TERMINATION_CONCLUSION_ACTION = 'submit-study-termination-conclusion'


class ProtocolDeviationViolationAction(Action):
    name = PROTOCOL_DEVIATION_VIOLATION_ACTION
    display_name = 'Submit Protocol Deviation / Violation Report'
    model = 'ambition_prn.protocoldeviationviolation'
    show_on_dashboard = True
    priority = HIGH_PRIORITY


class StudyTerminationConclusionAction(Action):
    name = STUDY_TERMINATION_CONCLUSION_ACTION
    display_name = 'Submit Study Termination/Conclusion Report'
    model = 'ambition_prn.studyterminationconclusion'
    show_on_dashboard = True
    priority = HIGH_PRIORITY


site_action_items.register(ProtocolDeviationViolationAction)
site_action_items.register(StudyTerminationConclusionAction)
