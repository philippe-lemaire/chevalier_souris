# Generated by Django 4.0.4 on 2022-05-19 06:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('creatures', '0004_remove_creature_variation_text'),
    ]

    operations = [
        migrations.AlterField(
            model_name='creature',
            name='armor',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
