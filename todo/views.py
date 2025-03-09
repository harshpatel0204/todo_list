from django.shortcuts import get_object_or_404, redirect, render

from .forms import TaskForm
from .models import Task


def task_list(request):
    tasks = Task.objects.all().order_by("-date")
    tasks_deleted = Task.all_objects.filter(deleted_at__isnull=False)
    return render(
        request, "task_list.html", {"tasks": tasks, "tasks_deleted": tasks_deleted}
    )


def task_create(request):
    if request.method == "POST":
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("task_list")
    else:
        form = TaskForm()
    return render(request, "task_form.html", {"form": form})


def task_update(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    if request.method == "POST":
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect("task_list")
    else:
        form = TaskForm(instance=task)
    return render(request, "task_form.html", {"form": form})


def task_delete(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    if request.method == "POST":
        task.soft_delete()
        return redirect("task_list")
    return render(request, "task_confirm_delete.html", {"task": task})
