# Generated by Django 2.1.4 on 2019-09-05 08:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='burnevent',
            name='etc',
            field=models.TextField(null=True),
        ),
    ]
