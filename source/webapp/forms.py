from django import forms
from webapp.models import Task, Project
from django.core.validators import BaseValidator


class CustomMaxLenValidator(BaseValidator):
    def __init__(self, limit_value):
        message = 'Максимальная длина поля %(limit_value)s. Выввели %(show_value)s символов'
        super().__init__(limit_value=limit_value, message=message)

    def compare(self, value, limit_value):
        return value > limit_value

    def clean(self, value):
        return len(value)


class CustomMinLenValidator(BaseValidator):
    def __init__(self, limit_value):
        message = 'Минимальная длина поля %(limit_value)s. Выввели %(show_value)s символов'
        super().__init__(limit_value=limit_value, message=message)

    def compare(self, value, limit_value):
        return value < limit_value

    def clean(self, value):
        return len(value)


class TaskForm(forms.ModelForm):
    title = forms.CharField(
        max_length=200,
        validators=(CustomMinLenValidator(2), CustomMaxLenValidator(200)))
    description = forms.CharField(
        max_length=3000,
        validators=(CustomMinLenValidator(2), CustomMaxLenValidator(3000)))

    class Meta:
        model = Task
        fields = {'title', 'description', 'status',
                  'task_types', 'completion_date'}
        labels = {
            'title': 'Заголовок',
            'description': 'Описание',
            'status': 'Статус',
            'task_types': 'Тип задачи',
            'completion_date': 'Выполнить до'
        }


class SearchForm(forms.Form):
    search = forms.CharField(max_length=20, required=False, label='Найти')


class ProjectForm(forms.ModelForm):
    title = forms.CharField(
        max_length=200,
        validators=(CustomMinLenValidator(2), CustomMaxLenValidator(200)))
    description = forms.CharField(
        max_length=3000,
        validators=(CustomMinLenValidator(2), CustomMaxLenValidator(3000)))

    class Meta:
        model = Project
        fields = {'title', 'description', 'start_date',
                  'completion_date'}
        labels = {
            'title': 'Заголовок',
            'description': 'Описание',
            'start_date': 'Дата начала',
            'completion_date': 'Дата окончания'
        }
