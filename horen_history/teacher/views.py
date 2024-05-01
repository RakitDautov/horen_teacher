from django.shortcuts import render
from django.core.paginator import Paginator

from .models import TeacherCard, ForParents, ForStudents, Methodically, HelpfulInformation


def index(request):
    card = TeacherCard.objects.get(id=1)

    return render(request, "index.html", {"card": card})


def parent(request):
    parents = Paginator(ForParents.objects.all(), 10)
    page_number = request.GET.get("page")
    page = parents.get_page(page_number)

    return render(request, "parents.html", {"parents": parents, "page": page})


def student(request):
    students = Paginator(ForStudents.objects.all(), 10)
    page_number = request.GET.get("page")
    page = students.get_page(page_number)

    return render(request, "student.html", {"students": students, "page": page})


def methodically(request):
    methodica = Paginator(Methodically.objects.all(), 10)
    page_number = request.GET.get("page")
    page = methodica.get_page(page_number)

    return render(request, "methodically.html", {"methodica": methodica, "page": page})


def info(request):
    info = HelpfulInformation.objects.all()
    paginator = Paginator(info, 10)
    page_number = request.GET.get("page")
    page = paginator.get_page(page_number)

    return render(request, "info.html", {"paginator": paginator, "page": page})
