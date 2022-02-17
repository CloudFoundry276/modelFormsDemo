from django.shortcuts import render
from modelFormsApp.forms import ProjectForm
from modelFormsApp.models import Project


# Create your views here.
def index(request):
    return render(request, "modelFormsApp/index.html")


def listProjects(request):
    projects_list = Project.objects.all()
    return render(request, "modelFormsApp/project_list.html", {"projects": projects_list})


def addProject(request):
    form = ProjectForm()
    if request.method == "POST":
        form = ProjectForm(request.POST)
        if form.is_valid():
            form.save()
        return index(request)
    return render(request, "modelFormsApp/project_add.html", {"form": form})
