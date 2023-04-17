from django.urls import path

from api.views.project import ProjectView
from api.views.task import TasktView

urlpatterns = [
    path("projects/<int:pk>", ProjectView.as_view(), name='project_detail'),
    path("tasks/<int:pk>", TasktView.as_view(), name='task_detail'),
]
