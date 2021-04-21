# Generated by Django 3.0.7 on 2020-07-10 18:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_depoimento'),
    ]

    operations = [
        migrations.AlterField(
            model_name='funcionario',
            name='git',
            field=models.URLField(blank=True, default='#', max_length=100, verbose_name='GitHub'),
        ),
        migrations.AlterField(
            model_name='funcionario',
            name='linkedin',
            field=models.URLField(blank=True, default='#', max_length=100, verbose_name='LinkedIn'),
        ),
    ]