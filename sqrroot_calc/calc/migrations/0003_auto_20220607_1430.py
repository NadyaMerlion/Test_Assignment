# Generated by Django 2.2.19 on 2022-06-07 11:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('calc', '0002_equation'),
    ]

    operations = [
        migrations.AlterField(
            model_name='equation',
            name='equation',
            field=models.CharField(choices=[('example', 'ax**2+bx+c=0')], max_length=2),
        ),
    ]
