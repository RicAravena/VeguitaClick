# Generated by Django 3.2.3 on 2022-06-18 05:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_auto_20220617_0113'),
    ]

    operations = [
        migrations.AlterField(
            model_name='alimento',
            name='idalimento',
            field=models.BigAutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='alimento',
            name='idtipoalimento',
            field=models.ForeignKey(db_column='idtipousuario', on_delete=django.db.models.deletion.DO_NOTHING, to='core.tipoalimento'),
        ),
        migrations.AlterField(
            model_name='tipoalimento',
            name='idtipoalimento',
            field=models.BigAutoField(primary_key=True, serialize=False),
        ),
    ]