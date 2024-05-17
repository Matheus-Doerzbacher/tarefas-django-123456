from django.urls import path
from tarefas import views

urlpatterns = [
    path('', views.index_view, name='index'),
    path('adicionar/', views.adicionar_view, name='adicionar'),
]
