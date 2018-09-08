# Generated by Django 2.0.1 on 2018-09-07 22:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_subscriptiongroup'),
        ('accounts', '0021_auto_20180831_1934'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProfileSubscriptionGroup',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.AddField(
            model_name='profile',
            name='subscription_groups',
            field=models.ManyToManyField(to='core.SubscriptionGroup'),
        ),
        migrations.AddField(
            model_name='profilesubscriptiongroup',
            name='profile',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.Profile'),
        ),
        migrations.AddField(
            model_name='profilesubscriptiongroup',
            name='subscription_group',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.SubscriptionGroup'),
        ),
    ]
