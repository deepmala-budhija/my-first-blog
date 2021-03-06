# Generated by Django 2.2.14 on 2020-07-20 08:52

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='LineListing',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('village', models.CharField(choices=[('Bhootgarh', 'Bhootgarh'), ('Majra', 'Majra')], max_length=100)),
                ('survey_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('person_name_collecting_date', models.CharField(max_length=500)),
                ('house_number', models.IntegerField()),
                ('household_number', models.CharField(max_length=1)),
            ],
        ),
    ]
