# Generated by Django 3.1.7 on 2021-04-06 11:46

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.db.models.manager


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MiddleModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Organization',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('organization_name', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Practitioner',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('Given0', models.CharField(max_length=20)),
                ('Given1', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='PractitionerRole',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('role_name', models.CharField(max_length=10, null=True)),
                ('organization', models.ManyToManyField(null=True, to='Application.Organization')),
                ('practitioner', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Application.practitioner')),
            ],
        ),
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=15, unique=True, verbose_name='login')),
                ('password', models.CharField(max_length=20, verbose_name='password')),
                ('test', models.CharField(max_length=20, verbose_name='test')),
                ('practitionerRoles', models.ManyToManyField(null=True, through='Application.MiddleModel', to='Application.PractitionerRole')),
            ],
            managers=[
                ('object', django.db.models.manager.Manager()),
            ],
        ),
        migrations.AddField(
            model_name='middlemodel',
            name='practitionerRoles',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Application.practitionerrole'),
        ),
        migrations.AddField(
            model_name='middlemodel',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
