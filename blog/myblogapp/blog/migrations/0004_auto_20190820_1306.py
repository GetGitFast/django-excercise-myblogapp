# Generated by Django 2.2.3 on 2019-08-20 03:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_announcement'),
    ]

    operations = [
        migrations.RenameField(
            model_name='announcement',
            old_name='Announcer',
            new_name='announcer',
        ),
    ]
