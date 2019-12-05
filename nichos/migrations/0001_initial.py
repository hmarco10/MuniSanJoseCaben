# Generated by Django 2.2.5 on 2019-10-04 14:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='owner',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('dpi', models.IntegerField()),
                ('phone', models.CharField(max_length=13)),
                ('address', models.CharField(max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='Predio',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('largo', models.FloatField()),
                ('ancho', models.FloatField()),
                ('nomenclatura', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Propietario',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=250)),
                ('dpi', models.IntegerField()),
                ('telefono', models.CharField(max_length=8)),
                ('direccion', models.CharField(max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('last_name', models.CharField(max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('number_credits', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='reservacion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titular', models.CharField(max_length=250)),
                ('espacios', models.IntegerField()),
                ('niveles', models.IntegerField()),
                ('ornato', models.IntegerField()),
                ('cancelado', models.BooleanField()),
                ('inspeccion', models.BooleanField()),
                ('fecha', models.DateTimeField(auto_now_add=True)),
                ('predio', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='nichos.Predio')),
                ('propietario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='nichos.Propietario')),
            ],
        ),
        migrations.CreateModel(
            name='Registration',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('schedule_time', models.TimeField()),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='nichos.Student')),
                ('subject', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='nichos.Subject')),
            ],
        ),
        migrations.AddField(
            model_name='predio',
            name='propietario',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='nichos.Propietario'),
        ),
    ]