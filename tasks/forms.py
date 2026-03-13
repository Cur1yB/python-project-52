from django import forms

from labels.models import Label
from statuses.models import Status
from tasks.models import Task
from users.models import User


class TaskForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["executor"].queryset = User.objects.all()
        self.fields["executor"].label_from_instance = (
            lambda obj: obj.get_full_name()
        )
        self.fields["labels"].queryset = Label.objects.all()

    class Meta:
        model = Task
        fields = ("name", "description", "status", "executor", "labels")
        widgets = {
            "name": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Имя",
                }
            ),
            "description": forms.Textarea(
                attrs={
                    "class": "form-control",
                    "placeholder": "Описание",
                }
            ),
            "status": forms.Select(
                attrs={
                    "class": "form-control",
                    "choices": Status,
                }
            ),
            "executor": forms.Select(
                attrs={
                    "class": "form-control",
                    "choices": User,
                }
            ),
            "labels": forms.SelectMultiple(
                attrs={
                    "class": "form-control",
                    "choices": Label,
                }
            ),
        }
        labels = {
            "name": "Имя",
            "description": "Описание",
            "status": "Статус",
            "executor": "Исполнитель",
            "labels": "Метки",
        }
