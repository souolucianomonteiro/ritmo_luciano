from django.urls import path
from domain.website.views.home_view import home_view

urlpatterns = [
    path('', home_view, name='home'),  # URL para a página inicial
    # Defina outras rotas aqui
]
