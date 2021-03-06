# Generated by Django 2.0.5 on 2018-07-06 15:50

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Counselor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sunStart', models.TimeField()),
                ('sunEnd', models.TimeField()),
                ('monStart', models.TimeField()),
                ('monEnd', models.TimeField()),
                ('tueStart', models.TimeField()),
                ('tueEnd', models.TimeField()),
                ('wedStart', models.TimeField()),
                ('wedEnd', models.TimeField()),
                ('thurStart', models.TimeField()),
                ('thurEnd', models.TimeField()),
                ('friStart', models.TimeField()),
                ('friEnd', models.TimeField()),
                ('satStart', models.TimeField()),
                ('satEnd', models.TimeField()),
                ('client', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
