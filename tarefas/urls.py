from django.urls import path
from tarefas import views

urlpatterns = [
    path('', views.index_view, name='index'),
    path('adicionar/', views.adicionar_view, name='adicionar'),
    path('excluir/<int:id_tarefa>', views.excluir_view, name='excluir'),
]
