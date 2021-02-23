# Generated by Django 2.0.8 on 2020-10-28 09:21

import dashboard.models
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0007_package_upstream_l10n_url'),
    ]

    operations = [
        migrations.CreateModel(
            name='CIPipeline',
            fields=[
                ('ci_pipeline_id', models.AutoField(primary_key=True, serialize=False)),
                ('ci_pipeline_uuid', models.UUIDField(default=uuid.uuid4, editable=False, unique=True)),
                ('ci_project_web_url', models.URLField(blank=True, max_length=500, null=True, verbose_name='Platform Project URL')),
                ('ci_project_details_json_str', models.TextField(blank=True, null=True)),
                ('ci_platform_jobs_json_str', models.TextField(blank=True, null=True)),
                ('ci_project_analyses_json_str', models.TextField(blank=True, null=True)),
                ('ci_project_import_settings_json_str', models.TextField(blank=True, null=True)),
                ('ci_project_assign_templates_json_str', models.TextField(blank=True, null=True)),
                ('ci_project_workflow_steps_json_str', models.TextField(blank=True, null=True)),
                ('ci_project_providers_json_str', models.TextField(blank=True, null=True)),
                ('ci_project_term_bases_json_str', models.TextField(blank=True, null=True)),
                ('ci_project_qa_checks_json_str', models.TextField(blank=True, null=True)),
                ('ci_project_trans_memory_json_str', models.TextField(blank=True, null=True)),
                ('ci_pipeline_visibility', models.BooleanField(default=True)),
                ('ci_package', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='dashboard.Package', verbose_name='Package')),
            ],
            options={
                'verbose_name': 'CI Pipeline',
                'db_table': 'ts_cipipeline',
            },
            bases=(dashboard.models.ModelMixin, models.Model),
        ),
        migrations.CreateModel(
            name='CIPlatformJob',
            fields=[
                ('ci_platform_job_id', models.AutoField(primary_key=True, serialize=False)),
                ('ci_platform_job_json_str', models.TextField(blank=True, null=True)),
                ('ci_platform_job_analyses_json_str', models.TextField(blank=True, null=True)),
                ('ci_platform_job_segments_json_str', models.TextField(blank=True, null=True)),
                ('ci_platform_job_status_changes_json_str', models.TextField(blank=True, null=True)),
                ('ci_platform_job_trans_resources_json_str', models.TextField(blank=True, null=True)),
                ('ci_platform_job_workflow_step_json_str', models.TextField(blank=True, null=True)),
                ('ci_platform_job_visibility', models.BooleanField(default=True)),
                ('ci_pipeline', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='dashboard.CIPipeline', to_field='ci_pipeline_uuid', verbose_name='CI Pipeline')),
            ],
            options={
                'verbose_name': 'CI Platform Job',
                'db_table': 'ts_ciplatformjob',
            },
            bases=(dashboard.models.ModelMixin, models.Model),
        ),
        migrations.AddField(
            model_name='platform',
            name='ci_status',
            field=models.BooleanField(default=False, verbose_name='CI Enable/Disable'),
        ),
        migrations.AddField(
            model_name='platform',
            name='token_api_json_str',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='platform',
            name='token_expiry',
            field=models.DateTimeField(blank=True, null=True, verbose_name='Auth Token Expiry'),
        ),
        migrations.AlterField(
            model_name='platform',
            name='auth_token_key',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='Auth Password/Token'),
        ),
        migrations.AddField(
            model_name='cipipeline',
            name='ci_platform',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='dashboard.Platform', verbose_name='Platform'),
        ),
        migrations.AddField(
            model_name='cipipeline',
            name='ci_pull_job_template',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='pull_template', to='dashboard.JobTemplate', verbose_name='Pull Job Template'),
        ),
        migrations.AddField(
            model_name='cipipeline',
            name='ci_push_job_template',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='push_template', to='dashboard.JobTemplate', verbose_name='Push Job Template'),
        ),
        migrations.AddField(
            model_name='cipipeline',
            name='ci_release',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='dashboard.Release', verbose_name='Release'),
        ),
        migrations.AddField(
            model_name='job',
            name='ci_pipeline',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='dashboard.CIPipeline', verbose_name='CI Pipeline'),
        ),
    ]
