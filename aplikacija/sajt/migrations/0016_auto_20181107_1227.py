# Generated by Django 2.1.2 on 2018-11-07 12:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sajt', '0015_auto_20181107_1210'),
    ]

    operations = [
        migrations.AlterField(
            model_name='prodaja',
            name='Velicina',
            field=models.CharField(choices=[('S', 'Male'), ('M', 'Srednje'), ('L', 'Velike')], max_length=4, null=True),
        ),
    ]