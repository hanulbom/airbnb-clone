# Generated by Django 2.2.5 on 2019-10-31 05:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rooms', '0004_auto_20191029_2303'),
    ]

    operations = [
        migrations.RenameField(
            model_name='room',
            old_name='ficilities',
            new_name='facilities',
        ),
    ]