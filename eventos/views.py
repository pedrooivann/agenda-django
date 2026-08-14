from django.shortcuts import render, redirect
from .models import Evento


def mostrar_home(request):

    if request.method == "POST":

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

        return redirect("home")

    eventos = Evento.objects.all().order_by("data_evento", "horario")

    return render(request, "index.html", {
        "eventos": eventos
    })


def editar_evento(request, id):

    evento = Evento.objects.get(id=id)

    if request.method == "POST":

        evento.titulo = request.POST["titulo"]
        evento.descricao = request.POST["descricao"]
        evento.data_evento = request.POST["data_evento"]
        evento.horario = request.POST["horario"]

        evento.save()

        return redirect("home")

    return redirect("home")


def excluir_evento(request, id):

    if request.method == "POST":

        evento = Evento.objects.get(id=id)

        evento.delete()

    return redirect("home")