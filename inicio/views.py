from django.shortcuts import render, redirect
def inicio_view(request):
    if request.method == "POST":
        level = request.POST.get("level")
        request.session["skill_level"] = level
        return redirect('main:main')  
    return render(request, 'main/skill_level.html')

