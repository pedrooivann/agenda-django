from django.urls import path
from . import views

urlpatterns = [
    path('', views.mostrar_home, name="home"),
        path("editar/<int:id>/", views.editar_evento, name="editar_evento"),
    path("excluir/<int:id>/", views.excluir_evento, name="excluir_evento"),
]