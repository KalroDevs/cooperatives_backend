# Generated by Django 5.0.7 on 2024-11-07 05:40

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_alter_customuser_options_alter_customuser_managers_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='county',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='users.county'),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='role',
            field=models.CharField(choices=[('admin', 'Administrator'), ('national', 'National'), ('county', 'County'), ('sp', 'Automation Service Provider'), ('fa', 'Funding Agency'), ('os', 'Other Stakeholders')], default='county', max_length=255),
        ),
    ]
