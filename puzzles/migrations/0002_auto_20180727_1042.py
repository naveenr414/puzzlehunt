# Generated by Django 2.0.7 on 2018-07-27 14:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('puzzles', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='submission',
            old_name='submitAnwer',
            new_name='submitAnswer',
        ),
    ]