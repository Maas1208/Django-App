# Generated by Django 5.1.2 on 2024-10-12 04:08

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bills', '0003_alter_gasto_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='gasto',
            name='usuario',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='gastos', to='bills.usuario'),
        ),
    ]
