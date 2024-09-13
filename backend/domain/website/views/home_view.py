from django.shortcuts import render


def home_view(request):
    # Renderiza o template home.html dentro de 'website'
    return render(request, 'website/home.html')
