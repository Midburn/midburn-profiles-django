# Generated by Django 2.2.9 on 2020-02-15 19:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tech_auth', '0004_blacklisteduser'),
    ]

    operations = [
        migrations.AlterField(
            model_name='burneruser',
            name='birthday',
            field=models.DateField(null=True),
        ),
    ]
