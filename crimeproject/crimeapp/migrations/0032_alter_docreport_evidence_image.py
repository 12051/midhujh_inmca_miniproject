# Generated by Django 4.2.4 on 2023-10-05 15:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crimeapp', '0031_rename_mail_docreport_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='docreport',
            name='evidence_image',
            field=models.FileField(blank=True, null=True, upload_to='evidence_images/'),
        ),
    ]