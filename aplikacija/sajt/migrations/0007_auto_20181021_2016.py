# Generated by Django 2.1.2 on 2018-10-21 20:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sajt', '0006_remove_prodaja_cijena'),
    ]

    operations = [
        migrations.AlterField(
            model_name='prodaja',
            name='Kolicina',
            field=models.DecimalField(decimal_places=2, max_digits=1000),
        ),
    ]
