# Generated by Django 5.0.7 on 2024-10-20 11:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_subcounty_ward'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='email',
            field=models.EmailField(max_length=254, unique=True),
        ),
    ]
