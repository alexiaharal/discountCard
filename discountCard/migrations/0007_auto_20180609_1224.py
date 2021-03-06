# Generated by Django 2.0.5 on 2018-06-09 11:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('discountCard', '0006_auto_20180609_1221'),
    ]

    operations = [
        migrations.AlterField(
            model_name='card',
            name='card_type',
            field=models.CharField(choices=[('Synolic Youth', 'Synolic Youth'), ('Synolic Personal', 'Synolic Personal'), ('Synolic Corporate', 'Synolic Corporate'), ('Synolic Visitors', 'Synolic Visitors')], default='', max_length=30),
        ),
        migrations.AlterField(
            model_name='profile',
            name='account_type',
            field=models.CharField(choices=[('Client', 'Client'), ('Partner', 'Partner')], default='Client', max_length=10),
        ),
        migrations.AlterField(
            model_name='profile',
            name='city',
            field=models.CharField(choices=[('Paphos', 'Paphos'), ('Nicosia', 'Nicosia'), ('Paralimni', 'Paralimni'), ('Limassol', 'Limassol'), ('Larnaka', 'Larnaka')], default='', max_length=20),
        ),
    ]
