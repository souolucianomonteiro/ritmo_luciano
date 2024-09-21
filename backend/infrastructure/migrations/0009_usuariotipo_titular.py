from django.db import migrations

def create_default_usuario_tipo(apps, schema_editor):
    UsuarioTipo = apps.get_model('infrastructure', 'UsuarioTipo')
    UsuarioTipo.objects.get_or_create(
        nome='Titular',
        defaults={
            'descricao': 'Titular',
            'status': 'ativo',  # Define um valor padrão para o status
        }
    )

class Migration(migrations.Migration):

    dependencies = [
        ('infrastructure', '0008_enderecomodel_localizacao_profissaomodel_and_more'),
    ]

    operations = [
        migrations.RunPython(create_default_usuario_tipo),
    ]
