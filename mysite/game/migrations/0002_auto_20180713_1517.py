# Generated by Django 2.0.6 on 2018-07-13 21:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='team',
            old_name='CenterOffense',
            new_name='CenterScoring',
        ),
        migrations.RenameField(
            model_name='team',
            old_name='PointGuardOffense',
            new_name='PointGuardScoring',
        ),
        migrations.RenameField(
            model_name='team',
            old_name='PowerForwardOffense',
            new_name='PowerForwardScoring',
        ),
        migrations.RenameField(
            model_name='team',
            old_name='ShootingGuardOffense',
            new_name='ShootingGuardScoring',
        ),
        migrations.RenameField(
            model_name='team',
            old_name='SmallForwardOffense',
            new_name='SmallForwardScoring',
        ),
    ]
