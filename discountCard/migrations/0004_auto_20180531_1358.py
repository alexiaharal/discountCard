# Generated by Django 2.0.5 on 2018-05-31 12:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('discountCard', '0003_auto_20180531_1357'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='account_type',
            field=models.CharField(choices=[('Client', 'Client'), ('Partner', 'Partner')], default='Client', max_length=10),
        ),
    ]
