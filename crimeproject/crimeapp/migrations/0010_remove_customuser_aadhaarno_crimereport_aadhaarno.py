# Generated by Django 4.2.4 on 2023-09-15 08:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crimeapp', '0009_customuser_is_law_customuser_is_normal'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customuser',
            name='aadhaarno',
        ),
        migrations.AddField(
            model_name='crimereport',
            name='aadhaarno',
            field=models.CharField(default='', max_length=12),
        ),
    ]