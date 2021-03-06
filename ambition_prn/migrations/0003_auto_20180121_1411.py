# Generated by Django 2.0.1 on 2018-01-21 12:11

import _socket
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django_revision.revision_field
import edc_base.model_fields.hostname_modification_field
import edc_base.model_fields.userfield
import edc_base.model_fields.uuid_auto_field
import edc_base.model_validators.date
import edc_base.sites.managers
import edc_base.utils
import edc_protocol.validators


class Migration(migrations.Migration):

    dependencies = [
        ('sites', '0002_alter_domain_unique'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('ambition_prn', '0002_auto_20180119_1312'),
    ]

    operations = [
        migrations.CreateModel(
            name='DeathReportTmg',
            fields=[
                ('created', models.DateTimeField(blank=True, default=edc_base.utils.get_utcnow)),
                ('modified', models.DateTimeField(blank=True, default=edc_base.utils.get_utcnow)),
                ('user_created', edc_base.model_fields.userfield.UserField(blank=True, help_text='Updated by admin.save_model', max_length=50, verbose_name='user created')),
                ('user_modified', edc_base.model_fields.userfield.UserField(blank=True, help_text='Updated by admin.save_model', max_length=50, verbose_name='user modified')),
                ('hostname_created', models.CharField(blank=True, default=_socket.gethostname, help_text='System field. (modified on create only)', max_length=60)),
                ('hostname_modified', edc_base.model_fields.hostname_modification_field.HostnameModificationField(blank=True, help_text='System field. (modified on every save)', max_length=50)),
                ('revision', django_revision.revision_field.RevisionField(blank=True, editable=False, help_text='System field. Git repository tag:branch:commit.', max_length=75, null=True, verbose_name='Revision')),
                ('device_created', models.CharField(blank=True, max_length=10)),
                ('device_modified', models.CharField(blank=True, max_length=10)),
                ('id', edc_base.model_fields.uuid_auto_field.UUIDAutoField(blank=True, editable=False, help_text='System auto field. UUID primary key.', primary_key=True, serialize=False)),
                ('report_status', models.CharField(choices=[('open', 'Open. Some information is still pending.'), ('closed', 'Closed. This report is complete')], max_length=25, verbose_name='What is the status of this report?')),
                ('report_closed_datetime', models.DateTimeField(blank=True, null=True, validators=[edc_base.model_validators.date.datetime_not_future], verbose_name='Date and time report closed.')),
                ('subject_identifier', models.CharField(max_length=50, verbose_name='Subject Identifier')),
                ('tracking_identifier', models.CharField(max_length=30, unique=True)),
                ('action_identifier', models.CharField(max_length=25, null=True)),
                ('report_datetime', models.DateTimeField(default=edc_base.utils.get_utcnow, validators=[edc_protocol.validators.datetime_not_before_study_start, edc_base.model_validators.date.datetime_not_future], verbose_name='Report Date')),
                ('cause_of_death', models.CharField(blank=True, choices=[('cryptococcal_meningitis', 'Cryptococcal meningitis'), ('Cryptococcal_meningitis_relapse_IRIS', 'Cryptococcal meningitis relapse/IRIS'), ('TB', 'TB'), ('bacteraemia', 'Bacteraemia'), ('bacterial_pneumonia', 'Bacterial pneumonia'), ('malignancy', 'Malignancy'), ('art_toxicity', 'ART toxicity'), ('IRIS_non_CM', 'IRIS non-CM'), ('diarrhea_wasting', 'Diarrhea/wasting'), ('unknown', 'Unknown'), ('OTHER', 'Other')], help_text='Main cause of death in the opinion of TMG member', max_length=50, null=True, verbose_name='Main cause of death')),
                ('cause_of_death_other', models.CharField(blank=True, max_length=100, null=True, verbose_name='If "Other" above, please specify')),
                ('cause_of_death_agreed', models.CharField(blank=True, choices=[('Yes', 'Yes'), ('No', 'No')], help_text='If No, explain in the narrative below', max_length=15, null=True, verbose_name='Is the cause of death agreed between study doctor and TMG member?')),
                ('tb_site', models.CharField(blank=True, choices=[('meningitis', 'Meningitis'), ('pulmonary', 'Pulmonary'), ('disseminated', 'Disseminated'), ('N/A', 'Not applicable')], default='N/A', max_length=25, verbose_name='If cause of death is TB, specify site of TB disease')),
                ('narrative', models.TextField(blank=True, null=True, verbose_name='Narrative')),
            ],
            options={
                'verbose_name': 'Death Report TMG',
                'verbose_name_plural': 'Death Report TMG',
            },
            managers=[
                ('on_site', edc_base.sites.managers.CurrentSiteManager()),
            ],
        ),
        migrations.CreateModel(
            name='HistoricalDeathReportTmg',
            fields=[
                ('created', models.DateTimeField(blank=True, default=edc_base.utils.get_utcnow)),
                ('modified', models.DateTimeField(blank=True, default=edc_base.utils.get_utcnow)),
                ('user_created', edc_base.model_fields.userfield.UserField(blank=True, help_text='Updated by admin.save_model', max_length=50, verbose_name='user created')),
                ('user_modified', edc_base.model_fields.userfield.UserField(blank=True, help_text='Updated by admin.save_model', max_length=50, verbose_name='user modified')),
                ('hostname_created', models.CharField(blank=True, default=_socket.gethostname, help_text='System field. (modified on create only)', max_length=60)),
                ('hostname_modified', edc_base.model_fields.hostname_modification_field.HostnameModificationField(blank=True, help_text='System field. (modified on every save)', max_length=50)),
                ('revision', django_revision.revision_field.RevisionField(blank=True, editable=False, help_text='System field. Git repository tag:branch:commit.', max_length=75, null=True, verbose_name='Revision')),
                ('device_created', models.CharField(blank=True, max_length=10)),
                ('device_modified', models.CharField(blank=True, max_length=10)),
                ('id', edc_base.model_fields.uuid_auto_field.UUIDAutoField(blank=True, db_index=True, editable=False, help_text='System auto field. UUID primary key.')),
                ('report_status', models.CharField(choices=[('open', 'Open. Some information is still pending.'), ('closed', 'Closed. This report is complete')], max_length=25, verbose_name='What is the status of this report?')),
                ('report_closed_datetime', models.DateTimeField(blank=True, null=True, validators=[edc_base.model_validators.date.datetime_not_future], verbose_name='Date and time report closed.')),
                ('subject_identifier', models.CharField(max_length=50, verbose_name='Subject Identifier')),
                ('tracking_identifier', models.CharField(db_index=True, max_length=30)),
                ('action_identifier', models.CharField(max_length=25, null=True)),
                ('report_datetime', models.DateTimeField(default=edc_base.utils.get_utcnow, validators=[edc_protocol.validators.datetime_not_before_study_start, edc_base.model_validators.date.datetime_not_future], verbose_name='Report Date')),
                ('cause_of_death', models.CharField(blank=True, choices=[('cryptococcal_meningitis', 'Cryptococcal meningitis'), ('Cryptococcal_meningitis_relapse_IRIS', 'Cryptococcal meningitis relapse/IRIS'), ('TB', 'TB'), ('bacteraemia', 'Bacteraemia'), ('bacterial_pneumonia', 'Bacterial pneumonia'), ('malignancy', 'Malignancy'), ('art_toxicity', 'ART toxicity'), ('IRIS_non_CM', 'IRIS non-CM'), ('diarrhea_wasting', 'Diarrhea/wasting'), ('unknown', 'Unknown'), ('OTHER', 'Other')], help_text='Main cause of death in the opinion of TMG member', max_length=50, null=True, verbose_name='Main cause of death')),
                ('cause_of_death_other', models.CharField(blank=True, max_length=100, null=True, verbose_name='If "Other" above, please specify')),
                ('cause_of_death_agreed', models.CharField(blank=True, choices=[('Yes', 'Yes'), ('No', 'No')], help_text='If No, explain in the narrative below', max_length=15, null=True, verbose_name='Is the cause of death agreed between study doctor and TMG member?')),
                ('tb_site', models.CharField(blank=True, choices=[('meningitis', 'Meningitis'), ('pulmonary', 'Pulmonary'), ('disseminated', 'Disseminated'), ('N/A', 'Not applicable')], default='N/A', max_length=25, verbose_name='If cause of death is TB, specify site of TB disease')),
                ('narrative', models.TextField(blank=True, null=True, verbose_name='Narrative')),
                ('history_date', models.DateTimeField()),
                ('history_change_reason', models.CharField(max_length=100, null=True)),
                ('history_type', models.CharField(choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
                ('history_id', edc_base.model_fields.uuid_auto_field.UUIDAutoField(primary_key=True, serialize=False)),
            ],
            options={
                'verbose_name': 'historical ',
                'ordering': ('-history_date', '-history_id'),
                'get_latest_by': 'history_date',
            },
        ),
        migrations.RemoveField(
            model_name='deathreporttmgone',
            name='death_report',
        ),
        migrations.RemoveField(
            model_name='deathreporttmgone',
            name='site',
        ),
        migrations.RemoveField(
            model_name='deathreporttmgtwo',
            name='death_report',
        ),
        migrations.RemoveField(
            model_name='deathreporttmgtwo',
            name='site',
        ),
        migrations.RemoveField(
            model_name='historicaldeathreporttmgone',
            name='death_report',
        ),
        migrations.RemoveField(
            model_name='historicaldeathreporttmgone',
            name='history_user',
        ),
        migrations.RemoveField(
            model_name='historicaldeathreporttmgone',
            name='site',
        ),
        migrations.RemoveField(
            model_name='historicaldeathreporttmgtwo',
            name='death_report',
        ),
        migrations.RemoveField(
            model_name='historicaldeathreporttmgtwo',
            name='history_user',
        ),
        migrations.RemoveField(
            model_name='historicaldeathreporttmgtwo',
            name='site',
        ),
        migrations.RenameField(
            model_name='deathreport',
            old_name='death_narrative',
            new_name='narrative',
        ),
        migrations.RenameField(
            model_name='historicaldeathreport',
            old_name='death_narrative',
            new_name='narrative',
        ),
        migrations.AlterField(
            model_name='deathreport',
            name='cause_of_death',
            field=models.CharField(choices=[('cryptococcal_meningitis', 'Cryptococcal meningitis'), ('Cryptococcal_meningitis_relapse_IRIS', 'Cryptococcal meningitis relapse/IRIS'), ('TB', 'TB'), ('bacteraemia', 'Bacteraemia'), ('bacterial_pneumonia', 'Bacterial pneumonia'), ('malignancy', 'Malignancy'), ('art_toxicity', 'ART toxicity'), ('IRIS_non_CM', 'IRIS non-CM'), ('diarrhea_wasting', 'Diarrhea/wasting'), ('unknown', 'Unknown'), ('OTHER', 'Other')], help_text='Main cause of death in the opinion of the local study doctor and local PI', max_length=50, verbose_name='Main cause of death'),
        ),
        migrations.AlterField(
            model_name='deathreport',
            name='cause_of_death_other',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='If "Other" above, please specify'),
        ),
        migrations.AlterField(
            model_name='deathreport',
            name='report_datetime',
            field=models.DateTimeField(default=edc_base.utils.get_utcnow, validators=[edc_protocol.validators.datetime_not_before_study_start, edc_base.model_validators.date.datetime_not_future], verbose_name='Report Date'),
        ),
        migrations.AlterField(
            model_name='deathreport',
            name='tb_site',
            field=models.CharField(choices=[('meningitis', 'Meningitis'), ('pulmonary', 'Pulmonary'), ('disseminated', 'Disseminated'), ('N/A', 'Not applicable')], default='N/A', max_length=25, verbose_name='If cause of death is TB, specify site of TB disease'),
        ),
        migrations.AlterField(
            model_name='historicaldeathreport',
            name='cause_of_death',
            field=models.CharField(choices=[('cryptococcal_meningitis', 'Cryptococcal meningitis'), ('Cryptococcal_meningitis_relapse_IRIS', 'Cryptococcal meningitis relapse/IRIS'), ('TB', 'TB'), ('bacteraemia', 'Bacteraemia'), ('bacterial_pneumonia', 'Bacterial pneumonia'), ('malignancy', 'Malignancy'), ('art_toxicity', 'ART toxicity'), ('IRIS_non_CM', 'IRIS non-CM'), ('diarrhea_wasting', 'Diarrhea/wasting'), ('unknown', 'Unknown'), ('OTHER', 'Other')], help_text='Main cause of death in the opinion of the local study doctor and local PI', max_length=50, verbose_name='Main cause of death'),
        ),
        migrations.AlterField(
            model_name='historicaldeathreport',
            name='cause_of_death_other',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='If "Other" above, please specify'),
        ),
        migrations.AlterField(
            model_name='historicaldeathreport',
            name='report_datetime',
            field=models.DateTimeField(default=edc_base.utils.get_utcnow, validators=[edc_protocol.validators.datetime_not_before_study_start, edc_base.model_validators.date.datetime_not_future], verbose_name='Report Date'),
        ),
        migrations.AlterField(
            model_name='historicaldeathreport',
            name='tb_site',
            field=models.CharField(choices=[('meningitis', 'Meningitis'), ('pulmonary', 'Pulmonary'), ('disseminated', 'Disseminated'), ('N/A', 'Not applicable')], default='N/A', max_length=25, verbose_name='If cause of death is TB, specify site of TB disease'),
        ),
        migrations.DeleteModel(
            name='DeathReportTmgOne',
        ),
        migrations.DeleteModel(
            name='DeathReportTmgTwo',
        ),
        migrations.DeleteModel(
            name='HistoricalDeathReportTmgOne',
        ),
        migrations.DeleteModel(
            name='HistoricalDeathReportTmgTwo',
        ),
        migrations.AddField(
            model_name='historicaldeathreporttmg',
            name='death_report',
            field=models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='ambition_prn.DeathReport'),
        ),
        migrations.AddField(
            model_name='historicaldeathreporttmg',
            name='history_user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='historicaldeathreporttmg',
            name='site',
            field=models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='sites.Site'),
        ),
        migrations.AddField(
            model_name='deathreporttmg',
            name='death_report',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='ambition_prn.DeathReport'),
        ),
        migrations.AddField(
            model_name='deathreporttmg',
            name='site',
            field=models.ForeignKey(editable=False, null=True, on_delete=django.db.models.deletion.PROTECT, to='sites.Site'),
        ),
    ]
