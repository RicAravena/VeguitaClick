# Generated by Django 3.2.3 on 2022-07-01 00:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='proveedor',
            options={'verbose_name_plural': 'Proveedores'},
        ),
        migrations.AlterModelOptions(
            name='tipoalimento',
            options={'verbose_name_plural': 'Tipo Alimentos'},
        ),
        migrations.AlterModelOptions(
            name='tipoproveedor',
            options={'verbose_name_plural': 'Tipo Proveedores'},
        ),
        migrations.AlterModelOptions(
            name='tipousuario',
            options={'verbose_name_plural': 'Tipo Cliente'},
        ),
        migrations.AlterModelOptions(
            name='transporte',
            options={'verbose_name': 'Transporte', 'verbose_name_plural': 'Transportes'},
        ),
        migrations.AlterModelOptions(
            name='usuario',
            options={'verbose_name': 'Cliente', 'verbose_name_plural': 'Clientes'},
        ),
        migrations.AddField(
            model_name='transporte',
            name='preciotransporte',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='alimento',
            name='codalimento',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Codigo alimento'),
        ),
        migrations.AlterField(
            model_name='alimento',
            name='idtipoalimento',
            field=models.ForeignKey(db_column='idtipousuario', on_delete=django.db.models.deletion.DO_NOTHING, to='core.tipoalimento', verbose_name='Tipo alimento'),
        ),
        migrations.AlterField(
            model_name='alimento',
            name='nomalimento',
            field=models.CharField(max_length=100, verbose_name='Nombre alimento'),
        ),
        migrations.AlterField(
            model_name='alimento',
            name='pesoalimento',
            field=models.DecimalField(blank=True, decimal_places=1, max_digits=38, null=True, verbose_name='Peso alimento'),
        ),
        migrations.AlterField(
            model_name='alimento',
            name='precioalimento',
            field=models.BigIntegerField(verbose_name='Precio alimento'),
        ),
        migrations.AlterField(
            model_name='proveedor',
            name='celuproveedor',
            field=models.IntegerField(blank=True, null=True, verbose_name='Celular proveedor'),
        ),
        migrations.AlterField(
            model_name='proveedor',
            name='direccionproveedor',
            field=models.CharField(blank=True, max_length=500, null=True, verbose_name='Direccion proveedor'),
        ),
        migrations.AlterField(
            model_name='proveedor',
            name='dvrutproveedor',
            field=models.BigIntegerField(verbose_name='Digito verificador proveedor'),
        ),
        migrations.AlterField(
            model_name='proveedor',
            name='idtipoproveedor',
            field=models.ForeignKey(db_column='idtipoproveedor', on_delete=django.db.models.deletion.DO_NOTHING, to='core.tipoproveedor', verbose_name='Tipo proveedor'),
        ),
        migrations.AlterField(
            model_name='proveedor',
            name='nomproveedor',
            field=models.CharField(max_length=150, verbose_name='Nombre proveedor'),
        ),
        migrations.AlterField(
            model_name='proveedor',
            name='rutproveedor',
            field=models.BigIntegerField(verbose_name='Rut provedor'),
        ),
        migrations.AlterField(
            model_name='proveedor',
            name='telefproveedor',
            field=models.IntegerField(blank=True, null=True, verbose_name='Telefono proveedor'),
        ),
        migrations.AlterField(
            model_name='tipoalimento',
            name='codtipoalimento',
            field=models.CharField(blank=True, max_length=150, null=True, verbose_name='Codigo tipo alimento'),
        ),
        migrations.AlterField(
            model_name='tipoalimento',
            name='nomtipoalimento',
            field=models.CharField(max_length=150, verbose_name='Nombre tipo alimento'),
        ),
        migrations.AlterField(
            model_name='tipoproveedor',
            name='nomtipoproveedor',
            field=models.CharField(blank=True, max_length=300, null=True, verbose_name='Nombre tipo proveedor'),
        ),
        migrations.AlterField(
            model_name='tipousuario',
            name='nomtipousuario',
            field=models.CharField(max_length=50, verbose_name='Nombre tipo Cliente'),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='apellidosusuario',
            field=models.CharField(max_length=500, verbose_name='Apellidos cliente'),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='correousuario',
            field=models.CharField(max_length=200, verbose_name='Correo cliente'),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='estadousuario',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Estado cliente'),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='fecharegistrousuario',
            field=models.DateField(blank=True, null=True, verbose_name='Fecha registro cliente'),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='idtipousuario',
            field=models.ForeignKey(db_column='idtipousuario', on_delete=django.db.models.deletion.DO_NOTHING, to='core.tipousuario', verbose_name='Tipo cliente'),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='nomusuario',
            field=models.CharField(max_length=100, verbose_name='Nombre cliente'),
        ),
    ]
