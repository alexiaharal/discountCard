# Generated by Django 2.0.5 on 2018-06-22 16:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('discountCard', '0008_auto_20180609_1225'),
    ]

    operations = [
        migrations.AddField(
            model_name='card',
            name='active',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='card',
            name='expired',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='card',
            name='card_type',
            field=models.CharField(choices=[('Synolic Visitors', 'Synolic Visitors'), ('Synolic Personal', 'Synolic Personal'), ('Synolic Youth', 'Synolic Youth'), ('Synolic Corporate', 'Synolic Corporate')], default='', max_length=30),
        ),
        migrations.AlterField(
            model_name='profile',
            name='account_type',
            field=models.CharField(choices=[('Partner', 'Partner'), ('Client', 'Client')], default='Client', max_length=10),
        ),
        migrations.AlterField(
            model_name='profile',
            name='city',
            field=models.CharField(choices=[('Paralimni', 'Paralimni'), ('Larnaka', 'Larnaka'), ('Limassol', 'Limassol'), ('Paphos', 'Paphos'), ('Nicosia', 'Nicosia')], default='', max_length=20),
        ),
    ]