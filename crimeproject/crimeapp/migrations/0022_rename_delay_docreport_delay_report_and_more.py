# Generated by Django 4.2.4 on 2023-09-25 21:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('crimeapp', '0021_rename_evidence_vid_aud_docreport_evidence_pic_vid_aud'),
    ]

    operations = [
        migrations.RenameField(
            model_name='docreport',
            old_name='delay',
            new_name='delay_report',
        ),
        migrations.RenameField(
            model_name='docreport',
            old_name='offenderDescription',
            new_name='descri',
        ),
        migrations.RenameField(
            model_name='docreport',
            old_name='victimDescription',
            new_name='victimDescri',
        ),
        migrations.RenameField(
            model_name='docreport',
            old_name='witnessInformation',
            new_name='witnessInfo',
        ),
    ]
