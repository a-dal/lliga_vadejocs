# Generated by Django 4.1.2 on 2022-10-09 21:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dominaria', '0007_alter_matchup_winner'),
    ]

    operations = [
        migrations.AlterField(
            model_name='matchup',
            name='games_won_by_p1',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='matchup',
            name='games_won_by_p2',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='matchup',
            name='winner',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='winner', to='dominaria.player'),
        ),
    ]
