# Generated by Django 3.2.7 on 2021-09-27 10:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0002_remove_tehtava_aika'),
    ]

    operations = [
        migrations.RenameField(
            model_name='tehtava',
            old_name='homma',
            new_name='tehtava',
        ),
    ]