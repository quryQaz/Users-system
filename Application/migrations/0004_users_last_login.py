# Generated by Django 3.1.7 on 2021-04-06 15:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Application', '0003_auto_20210406_1649'),
    ]

    operations = [
        migrations.AddField(
            model_name='users',
            name='last_login',
            field=models.DateTimeField(blank=True, null=True, verbose_name='last login'),
        ),
    ]
