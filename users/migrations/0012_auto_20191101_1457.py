# Generated by Django 2.2.5 on 2019-11-01 05:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0011_auto_20191101_1448'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='gender',
            field=models.CharField(blank=True, choices=[('other', 'Other'), ('male', 'Male'), ('female', 'Female')], max_length=10),
        ),
    ]