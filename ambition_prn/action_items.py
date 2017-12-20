from edc_action_item import Action, HIGH_PRIORITY, site_action_items


PROTOCOL_DEVIATION_VIOLATION_ACTION = 'submit-protocol-deviation-violation'
STUDY_TERMINATION_CONCLUSION_ACTION = 'submit-study-termination-conclusion'
STUDY_TERMINATION_CONCLUSION_ACTION_W10 = 'submit-w10-study-termination-conclusion'


class ProtocolDeviationViolationAction(Action):
    name = PROTOCOL_DEVIATION_VIOLATION_ACTION
    display_name = 'Submit Protocol Deviation / Violation Report'
    model = 'ambition_prn.protocoldeviationviolation'
    show_link_to_changelist = True
    admin_site_name = 'ambition_prn_admin'
    priority = HIGH_PRIORITY


class StudyTerminationConclusionAction(Action):
    name = STUDY_TERMINATION_CONCLUSION_ACTION
    display_name = 'Submit Study Termination/Conclusion Report'
    model = 'ambition_prn.studyterminationconclusion'
    show_link_to_changelist = True
    admin_site_name = 'ambition_prn_admin'
    priority = HIGH_PRIORITY


class StudyTerminationConclusionW10Action(Action):
    name = STUDY_TERMINATION_CONCLUSION_ACTION_W10
    display_name = 'Submit W10 Study Termination/Conclusion Report'
    model = 'ambition_prn.studyterminationconclusionw10'
    show_link_to_changelist = True
    admin_site_name = 'ambition_prn_admin'
    priority = HIGH_PRIORITY


site_action_items.register(ProtocolDeviationViolationAction)
site_action_items.register(StudyTerminationConclusionAction)
site_action_items.register(StudyTerminationConclusionW10Action)
