# Generated by Django 5.0.7 on 2024-08-17 14:29

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects_m', '0002_document'),
    ]

    operations = [
        migrations.AddField(
            model_name='document',
            name='project',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='documents', to='projects_m.project'),
        ),
    ]
