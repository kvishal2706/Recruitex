# Generated by Django 4.1.7 on 2023-02-25 09:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Jobs', '0004_tag_jobs_tag'),
    ]

    operations = [
        migrations.AddField(
            model_name='jobs',
            name='type',
            field=models.CharField(blank=True, choices=[('Online', 'Work-From-Home'), ('Offline', 'From Office')], max_length=20),
        ),
    ]
