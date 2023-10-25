# Generated by Django 4.2.4 on 2023-10-24 17:35

from django.conf import settings
import django.contrib.auth.models
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='CustomUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('name', models.CharField(default='', max_length=100)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('password', models.CharField(max_length=128)),
                ('is_normal', models.BooleanField(default=False)),
                ('is_law', models.BooleanField(default=False)),
                ('is_prison', models.BooleanField(default=False)),
                ('is_control', models.BooleanField(default=False)),
                ('is_verified', models.BooleanField(default=False)),
                ('verification_token', models.CharField(blank=True, max_length=100, null=True)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Aadhaar',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('aadhaar_number', models.CharField(max_length=12, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='CrimeReport',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reporter_name', models.CharField(max_length=100)),
                ('reporter_location', models.CharField(max_length=100)),
                ('off_type', models.CharField(blank=True, max_length=100, null=True)),
                ('datetime', models.DateTimeField(blank=True, null=True)),
                ('aadhaarno', models.CharField(default='', max_length=12)),
                ('description', models.TextField()),
                ('victimDescription', models.TextField(blank=True, null=True)),
                ('witnessInformation', models.TextField(blank=True, null=True)),
                ('offenderDescription', models.TextField(blank=True, null=True)),
                ('delay', models.TextField(blank=True, null=True)),
                ('status', models.CharField(blank=True, choices=[('Crime Reported', 'Crime Reported'), ('Preliminary Investigation completed', 'Preliminary Investigation completed'), ('Inquiry and Investigation in progress', 'Inquiry and Investigation in progress'), ('Inquiry and Investigation completed', 'Inquiry and Investigation completed'), ('Arrest and Detention', 'Arrest and Detention'), ('Case Closure in progress', 'Case Closure in progress'), ('Case Closed', 'Case Closed')], default='Crime Reported', max_length=100, null=True)),
                ('list_user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Inmate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('inmate_name', models.TextField(blank=True, max_length=100, null=True)),
                ('inmate_id', models.CharField(blank=True, max_length=10, null=True)),
                ('inmate_loc', models.CharField(choices=[('kanjirappally', 'Kanjirappally'), ('changanassery', 'Changanassery')], max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Jailor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='SpecLoc',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reporter_loc', models.CharField(max_length=100)),
                ('enforcement_loc', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='PublicReport',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('info_name', models.CharField(max_length=100)),
                ('mail', models.EmailField(blank=True, max_length=254, null=True)),
                ('reporter_location', models.CharField(max_length=100)),
                ('offen_type', models.CharField(blank=True, max_length=100, null=True)),
                ('datetime', models.DateTimeField(blank=True, null=True)),
                ('aadhno', models.CharField(default='', max_length=12)),
                ('description', models.TextField()),
                ('victimDescription', models.TextField(blank=True, null=True)),
                ('witnessInformation', models.TextField(blank=True, null=True)),
                ('offenderDescription', models.TextField(blank=True, null=True)),
                ('delay', models.TextField(blank=True, null=True)),
                ('status', models.CharField(choices=[('Crime Reported', 'Crime Reported'), ('Preliminary Investigation completed', 'Preliminary Investigation completed'), ('Inquiry and Investigation in progress', 'Inquiry and Investigation in progress'), ('Inquiry and Investigation completed', 'Inquiry and Investigation completed'), ('Arrest and Detention', 'Arrest and Detention'), ('Case Closure in progress', 'Case Closure in progress'), ('Case Closed', 'Case Closed')], default='Crime Reported', max_length=100)),
                ('list_user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('spec_location', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='crimeapp.specloc')),
            ],
        ),
        migrations.CreateModel(
            name='PrisonReport',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('loc_prison', models.CharField(choices=[('kanjirappally', 'Kanjirappally'), ('changanassery', 'Changanassery')], max_length=100)),
                ('nat_crime', models.CharField(choices=[('misconduct', 'Inmate Misconduct'), ('breach', 'Security Breaches'), ('harm', 'Harm')], max_length=100)),
                ('datetime', models.DateTimeField(blank=True, null=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('evidence_image', models.FileField(blank=True, null=True, upload_to='evidence_images/')),
                ('inmates', models.ManyToManyField(blank=True, to='crimeapp.inmate')),
            ],
        ),
        migrations.CreateModel(
            name='FIRFile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(upload_to='fir_files/')),
                ('crime_report', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='crimeapp.crimereport')),
            ],
        ),
        migrations.CreateModel(
            name='EvidenceCrimeReport',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('document_fir', models.FileField(blank=True, null=True, upload_to='evidence_fir/')),
                ('document_witness', models.FileField(blank=True, null=True, upload_to='evidence_witness/')),
                ('document_forensic', models.FileField(blank=True, null=True, upload_to='evidence_forensic/')),
                ('document_arrest', models.FileField(blank=True, null=True, upload_to='evidence_arrest/')),
                ('document_charge', models.FileField(blank=True, null=True, upload_to='evidence_charge/')),
                ('document_case', models.FileField(blank=True, null=True, upload_to='evidence_case/')),
                ('document_final', models.FileField(blank=True, null=True, upload_to='evidence_final/')),
                ('crime_idnum', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='crimeapp.crimereport')),
            ],
        ),
        migrations.CreateModel(
            name='DocReport',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('i_name', models.CharField(max_length=100)),
                ('ano', models.CharField(default='', max_length=12)),
                ('email', models.EmailField(blank=True, max_length=254, null=True)),
                ('descri', models.TextField(blank=True, null=True)),
                ('victimDescri', models.TextField(blank=True, null=True)),
                ('witnessInfo', models.TextField(blank=True, null=True)),
                ('delay_report', models.TextField(blank=True, null=True)),
                ('evidence_image', models.FileField(blank=True, null=True, upload_to='evidence_images/')),
                ('threat', models.CharField(blank=True, choices=[('Yes', 'Yes'), ('No', 'No')], default='No', max_length=3, verbose_name='Any kind of Threat or Violence faced')),
                ('status', models.CharField(blank=True, choices=[('Crime Reported', 'Crime Reported'), ('Preliminary Investigation completed', 'Preliminary Investigation completed'), ('Inquiry and Investigation in progress', 'Inquiry and Investigation in progress'), ('Inquiry and Investigation completed', 'Inquiry and Investigation completed'), ('Arrest and Detention', 'Arrest and Detention'), ('Case Closure in progress', 'Case Closure in progress'), ('Case Closed', 'Case Closed')], default='Crime Reported', max_length=100, null=True)),
                ('list_user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='crimereport',
            name='spec_location',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='crimeapp.specloc'),
        ),
        migrations.CreateModel(
            name='Appointment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('time', models.TimeField()),
                ('booked_by', models.EmailField(max_length=254)),
                ('jailor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='crimeapp.jailor')),
            ],
        ),
        migrations.CreateModel(
            name='AnonyReport',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reporter_location', models.CharField(max_length=100)),
                ('date', models.DateField()),
                ('time', models.TimeField()),
                ('location', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('offender_name', models.CharField(blank=True, max_length=100, null=True)),
                ('offender_vehiclenumber', models.CharField(blank=True, max_length=20, null=True)),
                ('witness_name', models.CharField(blank=True, max_length=100, null=True)),
                ('spec_location', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='crimeapp.specloc')),
            ],
        ),
    ]
