from django.apps import AppConfig as DjangoApponfig


class AppConfig(DjangoApponfig):
    name = 'ambition_prn'
    verbose_name = 'Ambition PRN'

    def ready(self):
        from .signals import study_termination_conclusion_on_post_save
        pass
