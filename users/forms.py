from django.contrib.auth.forms import UserCreationForm

from .models import User


class UserCreateForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields["password1"].label = "Пароль"               # NOSONAR
        self.fields["password2"].label = "Подтверждение пароля" # NOSONAR

        self.fields["password1"].help_text = ""                 # NOSONAR
        self.fields["password2"].help_text = (                  # NOSONAR
            "Для подтверждения, введите, пожалуйста, тот же пароль ещё раз."
        )

    class Meta(UserCreationForm.Meta):
        model = User
        fields = (
            "first_name",
            "last_name",
            "username",
            "password1", # NOSONAR
            "password2", # NOSONAR
        )
        labels = {
            "first_name": "Имя",
            "last_name": "Фамилия",
            "username": "Имя пользователя",
            "password1": "Пароль",               # NOSONAR
            "password2": "Подтверждение пароля", # NOSONAR
        }
        help_texts = {
            "username": "",
            "password1": "", # NOSONAR
            "password2": "", # NOSONAR
        }

    def clean_username(self):
        username = self.cleaned_data["username"]
        return username
