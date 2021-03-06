# Generated by Django 2.0.6 on 2018-06-08 23:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Docente',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cedula', models.IntegerField()),
                ('nombre', models.CharField(max_length=30)),
                ('apellido', models.CharField(max_length=30)),
                ('celular', models.CharField(max_length=30)),
                ('titulo', models.CharField(max_length=30)),
                ('correo', models.EmailField(max_length=254)),
                ('foto', models.ImageField(upload_to='foto/')),
            ],
        ),
        migrations.CreateModel(
            name='Estudiante',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigo', models.IntegerField()),
                ('nombre', models.CharField(max_length=30)),
                ('apellido', models.CharField(max_length=30)),
                ('celular', models.CharField(max_length=30)),
                ('correo', models.EmailField(max_length=254)),
                ('foto', models.ImageField(upload_to='foto/')),
                ('docente', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='rol.Docente')),
            ],
        ),
        migrations.CreateModel(
            name='Materia',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigo', models.IntegerField()),
                ('nombre', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Nota',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('logro', models.CharField(max_length=100, null=True)),
                ('nota1', models.DecimalField(decimal_places=2, max_digits=3)),
                ('nota2', models.DecimalField(decimal_places=2, max_digits=3)),
                ('nota3', models.DecimalField(decimal_places=2, max_digits=3)),
                ('docente', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='rol.Docente')),
                ('estudiante', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='rol.Estudiante')),
                ('materia', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='rol.Materia')),
            ],
        ),
        migrations.AddField(
            model_name='estudiante',
            name='materias',
            field=models.ManyToManyField(to='rol.Materia'),
        ),
    ]
