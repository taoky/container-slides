# Generated by Django 2.1.12 on 2019-10-14 14:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('frontend', '0002_auto_20191010_0025'),
    ]

    operations = [
        migrations.AddField(
            model_name='page',
            name='js',
            field=models.TextField(blank=True, help_text='会被放入 <code>script</code> 的 JS'),
        ),
    ]
