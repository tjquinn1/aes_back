# Generated by Django 2.0.5 on 2018-08-27 00:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('consul', '0011_auto_20180827_0038'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='athCounseling',
            field=models.CharField(blank=True, max_length=20),
        ),
        migrations.AlterField(
            model_name='contact',
            name='domViolence',
            field=models.CharField(blank=True, max_length=20),
        ),
        migrations.AlterField(
            model_name='contact',
            name='dui',
            field=models.CharField(blank=True, max_length=20),
        ),
        migrations.AlterField(
            model_name='contact',
            name='empAssistance',
            field=models.CharField(blank=True, max_length=20),
        ),
        migrations.AlterField(
            model_name='contact',
            name='famCounseling',
            field=models.CharField(blank=True, max_length=20),
        ),
        migrations.AlterField(
            model_name='contact',
            name='name',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='contact',
            name='partnership',
            field=models.CharField(blank=True, max_length=25),
        ),
        migrations.AlterField(
            model_name='contact',
            name='phone',
            field=models.CharField(max_length=11),
        ),
        migrations.AlterField(
            model_name='contact',
            name='teenHelp',
            field=models.CharField(blank=True, max_length=20),
        ),
        migrations.AlterField(
            model_name='contact',
            name='title',
            field=models.CharField(max_length=20),
        ),
    ]
