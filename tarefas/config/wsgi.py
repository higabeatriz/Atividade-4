"""
WSGI config for seu_projeto project.

It exposes the WSGI callable as a module-level variable named ``application``.
"""

import os

# Importa a função correta para WSGI
from django.core.wsgi import get_wsgi_application

# Define o caminho para o seu arquivo settings
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings') 

# Define a variável 'application' que o Django espera
application = get_wsgi_application()