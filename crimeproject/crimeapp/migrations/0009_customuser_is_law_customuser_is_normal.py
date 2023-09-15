# Generated by Django 4.2.4 on 2023-09-15 06:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crimeapp', '0008_crimereport_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='is_law',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='customuser',
            name='is_normal',
            field=models.BooleanField(default=False),
        ),
    ]
