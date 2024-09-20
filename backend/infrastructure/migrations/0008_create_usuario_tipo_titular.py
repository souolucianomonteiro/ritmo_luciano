# pylint: disable=unused-argument

from django.db import migrations


def create_default_usuario_tipo(apps, schema_editor):
    UsuarioTipo = apps.get_model('infrastructure', 'UsuarioTipo')
    UsuarioTipo.objects.get_or_create(id=1, nome='Titular', descricao='Usuário Titular')


class Migration(migrations.Migration):

    dependencies = [
        ('infrastructure', '0001_initial'),  # Substitua pela sua migration inicial
    ]

    operations = [
        migrations.RunPython(create_default_usuario_tipo),
    ]
