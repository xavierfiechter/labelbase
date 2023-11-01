# Generated by Django 3.2.20 on 2023-10-18 22:59

from django.db import migrations, models
import django_cryptography.fields


class Migration(migrations.Migration):

    dependencies = [
        ('labelbase', '0007_labelbase_network'),
    ]

    operations = [
        migrations.AlterField(
            model_name='label',
            name='label',
            field=django_cryptography.fields.encrypt(models.CharField(blank=True, default='', max_length=255)),
        ),
    ]
