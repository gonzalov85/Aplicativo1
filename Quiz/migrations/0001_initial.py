# Generated by Django 3.2.6 on 2021-08-24 02:34

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.TextField(verbose_name='Categoria')),
            ],
        ),
        migrations.CreateModel(
            name='ElegirRespuesta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('correcta', models.BooleanField(default=False, verbose_name='¿Es esta la respuesta correcta?')),
                ('texto', models.TextField(default=None, null=True, verbose_name='Texto de la respuesta')),
            ],
        ),
        migrations.CreateModel(
            name='Pregunta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('texto', models.TextField(verbose_name='Texto de la pregunta')),
                ('max_puntaje', models.DecimalField(decimal_places=2, default=3, max_digits=6, verbose_name='Maximo Puntaje')),
                ('categoria', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='Quiz.categoria')),
            ],
        ),
        migrations.CreateModel(
            name='QuizUsuario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('puntaje_total', models.DecimalField(decimal_places=2, default=0, max_digits=10, null=True, verbose_name='puntaje total')),
                ('usuario', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='PreguntasRespondidas',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('correcta', models.BooleanField(default=False, verbose_name='¿Es estal a respuesta correcta?')),
                ('puntaje_obtenido', models.DecimalField(decimal_places=2, default=0, max_digits=6, verbose_name='Puntaje Obtenido')),
                ('pregunta', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Quiz.pregunta')),
                ('quizUser', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='intentos', to='Quiz.quizusuario')),
                ('respuesta', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Quiz.elegirrespuesta')),
            ],
        ),
        migrations.AddField(
            model_name='elegirrespuesta',
            name='pregunta',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='opciones', to='Quiz.pregunta'),
        ),
    ]
