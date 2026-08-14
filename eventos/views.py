from django.shortcuts import render
from .models import Evento

def mostrar_home(request):

    if request.method == "POST":
        print("POST RECEBIDO:", request.POST)

        titulo = request.POST["titulo"]
        descricao = request.POST["descricao"]
        data_evento = request.POST["data_evento"]
        horario = request.POST["horario"]

        Evento.objects.create(
            titulo=titulo,
            descricao=descricao,
            data_evento=data_evento,
            horario=horario
        )

    eventos = Evento.objects.all()

    return render(request, "index.html", {
        "eventos": eventos
    })