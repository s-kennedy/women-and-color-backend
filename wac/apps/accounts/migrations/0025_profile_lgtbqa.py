# Generated by Django 2.0.2 on 2018-11-25 21:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0024_auto_20181010_1806'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='lgtbqa',
            field=models.NullBooleanField(),
        ),
    ]