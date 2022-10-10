# Generated by Django 4.1.2 on 2022-10-08 23:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dominaria', '0006_alter_matchup_winner'),
    ]

    operations = [
        migrations.AlterField(
            model_name='matchup',
            name='winner',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='winner', to='dominaria.player'),
        ),
    ]
