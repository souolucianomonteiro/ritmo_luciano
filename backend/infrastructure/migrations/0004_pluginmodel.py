# Generated by Django 5.0.9 on 2024-09-15 16:06

import django.db.models.deletion
import uuid
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('infrastructure', '0003_alter_categoriamodel_options_and_more'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='PluginModel',
            fields=[
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('is_deleted', models.BooleanField(default=False)),
                ('deleted_at', models.DateTimeField(blank=True, null=True)),
                ('is_active', models.BooleanField(default=True)),
                ('inactivated_at', models.DateTimeField(blank=True, null=True)),
                ('status', models.CharField(choices=[('active', 'Active'), ('inactive', 'Inactive'), ('pending', 'Pending'), ('completed', 'Completed')], default='active', max_length=10)),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('nome', models.CharField(max_length=255)),
                ('versao', models.CharField(max_length=50)),
                ('descricao', models.TextField(blank=True, null=True)),
                ('documentacao', models.TextField(blank=True, null=True)),
                ('permissoes', models.JSONField(default=list)),
                ('historico_modificacoes', models.JSONField(default=list)),
                ('tags', models.JSONField(default=list)),
                ('dependencias', models.JSONField(default=list)),
                ('artefato_plugin', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='infrastructure.artefatopluginmodel')),
                ('categoria', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='infrastructure.categoriamodel')),
                ('created_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='created_%(class)s_set', to=settings.AUTH_USER_MODEL)),
                ('tipo_plugin', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='infrastructure.tipopluginmodel')),
                ('updated_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='updated_%(class)s_set', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Plugin',
                'verbose_name_plural': 'Plugins',
                'db_table': 'infrastructure_plugin',
            },
        ),
    ]
