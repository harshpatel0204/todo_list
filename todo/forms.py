from django import forms

from .models import Task


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ["date", "start_time", "end_time", "description"]
        widgets = {
            "date": forms.DateInput(attrs={"type": "date", "class": "form-control"}),
            "start_time": forms.TimeInput(
                attrs={"type": "time", "class": "form-control"}
            ),
            "end_time": forms.TimeInput(
                attrs={"type": "time", "class": "form-control"}
            ),
            "description": forms.Textarea(attrs={"rows": 2, "class": "form-control"}),
        }
