# Generated by Django 3.1.5 on 2021-01-23 11:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('participantes', '0006_auto_20210115_1929'),
    ]

    operations = [
        migrations.CreateModel(
            name='Equipe',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=150)),
                ('descricao', models.TextField()),
                ('lider', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='lider_equipe', to='participantes.participante')),
                ('membros', models.ManyToManyField(related_name='membros_equipe', to='participantes.Participante')),
            ],
        ),
    ]
