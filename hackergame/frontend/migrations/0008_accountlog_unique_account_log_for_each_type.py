# Generated by Django 4.2.5 on 2023-10-12 18:06

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("frontend", "0007_accountlog_specialprofileusedrecord_and_more"),
    ]

    operations = [
        migrations.AddConstraint(
            model_name="accountlog",
            constraint=models.UniqueConstraint(
                fields=("account", "content_type"),
                name="unique_account_log_for_each_type",
            ),
        ),
    ]
