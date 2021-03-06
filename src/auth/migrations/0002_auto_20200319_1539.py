# Generated by Django 3.0.4 on 2020-03-19 13:39

from django.db import migrations, models
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('tech_auth', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='burneruser',
            options={'verbose_name': 'user', 'verbose_name_plural': 'users'},
        ),
        migrations.AlterField(
            model_name='burneruser',
            name='address',
            field=models.TextField(default=None, null=True),
        ),
        migrations.AlterField(
            model_name='burneruser',
            name='city',
            field=models.TextField(default=None, null=True),
        ),
        migrations.AlterField(
            model_name='burneruser',
            name='email',
            field=models.EmailField(db_index=True, max_length=254, unique=True, verbose_name='email address'),
        ),
        migrations.AlterField(
            model_name='burneruser',
            name='primary_phone_number',
            field=phonenumber_field.modelfields.PhoneNumberField(blank=True, default=None, max_length=128, null=True, region=None),
        ),
        migrations.AlterUniqueTogether(
            name='burneruser',
            unique_together=set(),
        ),
        migrations.RemoveField(
            model_name='burneruser',
            name='identification_number',
        ),
        migrations.RemoveField(
            model_name='burneruser',
            name='identification_type',
        ),
        migrations.RemoveField(
            model_name='burneruser',
            name='passport_country',
        ),
    ]
