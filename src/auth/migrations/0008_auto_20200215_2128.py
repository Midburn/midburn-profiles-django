# Generated by Django 2.2.9 on 2020-02-15 21:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tech_auth', '0007_burneruser_year_in_school'),
    ]

    operations = [
        migrations.AlterField(
            model_name='burneruser',
            name='year_in_school',
            field=models.CharField(choices=[('tz', 'tz'), ('ps', 'ps')], default='tz', max_length=2),
        ),
    ]
