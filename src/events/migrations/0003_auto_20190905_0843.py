# Generated by Django 2.1.4 on 2019-09-05 08:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0002_auto_20190905_0843'),
    ]

    operations = [
        migrations.AlterField(
            model_name='burnevent',
            name='etc',
            field=models.TextField(blank=True, null=True),
        ),
    ]
