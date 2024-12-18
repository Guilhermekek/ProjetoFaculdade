# Generated by Django 5.1.3 on 2024-12-05 14:50

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Treino',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('descricao', models.TextField(blank=True, null=True)),
                ('data_criacao', models.DateTimeField(auto_now_add=True)),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Exercicio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('repeticoes', models.PositiveIntegerField()),
                ('tempo_descanso', models.DurationField(help_text='Tempo de descanso entre repetições (hh:mm:ss)')),
                ('peso', models.DecimalField(decimal_places=2, help_text='Peso em kg', max_digits=5)),
                ('descricao', models.TextField(blank=True, null=True)),
                ('treino', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='exercicios', to='Academia.treino')),
            ],
        ),
    ]
