# Generated by Django 5.0.7 on 2024-10-22 06:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cooperatives', '0006_dashboards_scope'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bookkeeperregister',
            name='book_keeper_national_id',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
    ]