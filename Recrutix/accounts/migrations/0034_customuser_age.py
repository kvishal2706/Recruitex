# Generated by Django 4.1.7 on 2023-04-02 09:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("accounts", "0033_customuser_experience"),
    ]

    operations = [
        migrations.AddField(
            model_name="customuser",
            name="age",
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
    ]
