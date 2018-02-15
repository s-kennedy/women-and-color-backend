# Generated by Django 2.0.1 on 2018-02-09 05:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_profilelocation_profiletopic'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='page',
            field=models.CharField(blank=True, default='registration', max_length=25, null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='pronouns',
            field=models.CharField(blank=True, choices=[('he', 'he'), ('she', 'she'), ('they', 'they')], max_length=10, null=True),
        ),
    ]
