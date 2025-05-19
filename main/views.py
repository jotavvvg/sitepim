from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
def inicio_view(request):
    if request.method == "POST":
        level = request.POST.get("level")
        request.session["skill_level"] = level
        return redirect('main:main')  
    return render(request, 'main/skill_level.html')
@login_required
def main_view(request):
    level = request.session.get("skill_level")
    if not level:
        return redirect('main:inicio')
    return render(request, 'main/main.html', {'level': level})
@login_required
def aulas_view(request):
    return render(request, 'main/aulas.html')
@login_required
def dicas_view(request):
    return render(request, 'main/dicas.html')
@login_required
def perfil_view(request):
    return render(request, 'main/perfil.html')
def logout_view(request):
    logout(request)
    return redirect('/')  
@login_required
def main_page(request):
    level = request.session.get('level')  
    return render(request, 'main/main.html', {
        'level': level,
         'user': request.user,  
    })
def niveis_view(request):
    if request.method == "POST":
        level = request.POST.get("level")
        request.session["skill_level"] = level
        return redirect('main:inicio')  
    return render(request, 'main/skill_level.html')
@login_required
def atividades_view(request):
    return render(request, 'main/atividades.html')
@login_required
def atividade_detail_view(request, atividade_slug):
    template_map = {
        'partes-computador': 'main/atividades/partes_computador.html',
        'senha-segura': 'main/atividades/senha_segura.html',
        'sites-confiaveis': 'main/atividades/sites_confiaveis.html',
        'envia-email': 'main/atividades/envia_email.html',
        'anexo-email': 'main/atividades/anexo_email.html',
        'privacidade-redes': 'main/atividades/privacidade_redes.html',
        'redes-sociais': 'main/atividades/redes_sociais.html',
    }
    template = template_map.get(atividade_slug)
    if not template:
        return render(request, 'main/atividades/404.html', status=404)
    return render(request, template)

