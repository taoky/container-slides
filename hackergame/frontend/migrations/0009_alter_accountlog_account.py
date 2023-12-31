# Generated by Django 4.2.5 on 2023-10-14 16:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("frontend", "0008_accountlog_unique_account_log_for_each_type"),
    ]

    operations = [
        migrations.AlterField(
            model_name="accountlog",
            name="account",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="frontend.account"
            ),
        ),
    ]
