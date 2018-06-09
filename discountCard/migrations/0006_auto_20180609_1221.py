# Generated by Django 2.0.5 on 2018-06-09 11:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('discountCard', '0005_auto_20180609_1216'),
    ]

    operations = [
        migrations.AddField(
            model_name='card',
            name='card_type',
            field=models.CharField(choices=[('Synolic Youth', 'Synolic Youth'), ('Synolic Corporate', 'Synolic Corporate'), ('Synolic Visitors', 'Synolic Visitors'), ('Synolic Personal', 'Synolic Personal')], default='', max_length=30),
        ),
        migrations.AlterField(
            model_name='profile',
            name='city',
            field=models.CharField(choices=[('Limassol', 'Limassol'), ('Paralimni', 'Paralimni'), ('Nicosia', 'Nicosia'), ('Paphos', 'Paphos'), ('Larnaka', 'Larnaka')], default='', max_length=20),
        ),
    ]