#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys
from django.core.management import execute_from_command_line  # Importação movida para o topo


def main():
    """Run administrative tasks."""
    # Configura o módulo de configurações do Django
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'backend.ritmo_digital.settings')
    try:
        execute_from_command_line(sys.argv)
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc


if __name__ == '__main__':
    main()
