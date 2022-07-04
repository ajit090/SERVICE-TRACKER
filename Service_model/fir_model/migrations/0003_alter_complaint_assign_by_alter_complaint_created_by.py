# Generated by Django 4.0.4 on 2022-07-02 06:13

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('fir_model', '0002_alter_complaint_created_by'),
    ]

    operations = [
        migrations.AlterField(
            model_name='complaint',
            name='assign_by',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='Assigned_by', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='complaint',
            name='created_by',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='Created_by', to=settings.AUTH_USER_MODEL),
        ),
    ]