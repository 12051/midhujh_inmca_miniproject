# Generated by Django 4.2.4 on 2023-09-12 04:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crimeapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='username',
            field=models.CharField(default='', max_length=20, unique=True),
        ),
    ]