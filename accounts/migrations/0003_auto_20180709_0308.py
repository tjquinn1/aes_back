# Generated by Django 2.0.5 on 2018-07-09 03:08

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_user_middle_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='token',
        ),
        migrations.AddField(
            model_name='user',
            name='jwt_secret',
            field=models.UUIDField(default=uuid.uuid4),
        ),
    ]
