# Generated by Django 3.0.7 on 2020-07-10 18:27

import core.models
from django.db import migrations, models
import stdimage.models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_auto_20200710_1226'),
    ]

    operations = [
        migrations.CreateModel(
            name='Depoimento',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateField(auto_now_add=True, verbose_name='Data de Criação')),
                ('modified_at', models.DateField(auto_now=True, verbose_name='Data de Atualização')),
                ('active', models.BooleanField(default=True, verbose_name='Ativo?')),
                ('nome', models.CharField(max_length=100, verbose_name='Nome')),
                ('profissao', models.CharField(max_length=100, verbose_name='Profissão')),
                ('comentario', models.TextField(max_length=200, verbose_name='Comentário')),
                ('imagem', stdimage.models.StdImageField(upload_to=core.models.get_file_path, verbose_name='Imagem')),
            ],
            options={
                'verbose_name': 'Depoimento',
                'verbose_name_plural': 'Depoimentos',
            },
        ),
    ]