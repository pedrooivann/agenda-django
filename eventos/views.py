from django.shortcuts import render

def mostrar_home (request):
    return render(request, "index.html")