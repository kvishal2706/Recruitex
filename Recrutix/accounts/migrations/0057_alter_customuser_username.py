# Generated by Django 4.1.7 on 2023-04-03 19:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("accounts", "0056_alter_customuser_username"),
    ]

    operations = [
        migrations.AlterField(
            model_name="customuser",
            name="username",
            field=models.CharField(max_length=100, unique=True),
        ),
    ]
