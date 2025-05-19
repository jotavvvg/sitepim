from django.urls import path
from . import views
app_name = 'main'
urlpatterns = [
    path('', views.main_view, name='inicio'),  
    path('niveis/', views.niveis_view, name='niveis'),  
    path('aulas/', views.aulas_view, name='aulas'),
    path('atividades/', views.atividades_view, name='atividades'),  
    path('atividade/<slug:atividade_slug>/', views.atividade_detail_view, name='atividade'),
    path('dicas/', views.dicas_view, name='dicas'),
    path('perfil/', views.perfil_view, name='perfil'),
    path('logout/', views.logout_view, name='logout'),
]

