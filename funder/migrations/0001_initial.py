# Generated by Django 3.0.7 on 2020-06-12 20:00

from django.conf import settings
import django.contrib.auth.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Funder',
            fields=[
                ('customuser_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('organization_name', models.CharField(max_length=120)),
                ('sector_of_operation', models.CharField(max_length=120)),
                ('type_of_organization', models.CharField(choices=[('Goverment', 'Goverment organization'), ('Non-Goverment', 'Non-Goverment organization'), ('private', 'private organization'), ('international', 'international organization')], default='private', max_length=120)),
                ('name_of_contact_person', models.CharField(max_length=120)),
                ('address', models.CharField(max_length=120)),
                ('contact_number1', models.CharField(max_length=120)),
                ('contact_numder2', models.CharField(max_length=120)),
                ('email_address', models.CharField(max_length=120)),
                ('website', models.CharField(max_length=120)),
                ('type_of_financing', models.CharField(choices=[('Credit', 'Credit financing'), ('Grant', 'Grant financing'), ('In Kind', 'In Kind financing'), ('Research', 'Researc financing')], default='Grant', max_length=120)),
                ('primary_funding_agency1', models.CharField(max_length=120)),
                ('primary_funding_agency2', models.CharField(max_length=120)),
                ('primary_funding_agency3', models.CharField(max_length=120)),
                ('terms_and_conditions', models.TextField(max_length=380)),
                ('purpose_for_financing', models.CharField(max_length=120)),
                ('geographical_preference', models.CharField(max_length=120)),
                ('funding_ceiling', models.IntegerField()),
                ('fund_startups_or_ongoing', models.CharField(choices=[('Startup Projects', 'Startup projects'), ('Ongoing Projects', 'Ongoing projects'), ('all', 'all projects types')], default='all', max_length=120)),
                ('eligibility_criteria_of_SME', models.TextField(max_length=380)),
                ('deadline_of_application', models.DateTimeField()),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            bases=('user.customuser',),
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
    ]
