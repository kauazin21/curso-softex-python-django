from django.urls import path
from . import views # O '.' importa as 'views' do app atual
urlpatterns = [
# Quando a URL for a raiz (''), chame a função 'home' de 'views.py'
path('', views.home, name='home'),

path('tarefa/<int:pk>/concluir/', views.concluir_tarefa, name='concluir_tarefa'),
# Ex: /tarefa/5/deletar/
path('tarefa/<int:pk>/deletar/', views.deletar_tarefa, name='deletar_tarefa'),

path('register/', views.register, name='register'),

]
