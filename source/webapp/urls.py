from django.urls import path
from webapp.views.base import IndexView, IndexRedirectView
from webapp.views.tasks import TaskDetail, TaskUpdateView, TaskDeleteView, TaskCreateView
from webapp.views.projects import ProjectDetail, ProjectUpdateView, ProjectDeleteView, ProjectCreateView, ProjectIndexView


urlpatterns = [
    path("",  IndexView.as_view(), name='index'),
    path("task/", IndexRedirectView.as_view(), name='task_index_redirect'),
    path("task/add/", TaskCreateView.as_view(), name='task_add'),
    path("task/<int:pk>", TaskDetail.as_view(), name='task_detail'),
    path("task/<int:pk>/update/", TaskUpdateView.as_view(), name='task_update'),
    path("task/<int:pk>/delete/", TaskDeleteView.as_view(), name='task_delete'),
    path("project/",  ProjectIndexView.as_view(), name='project_index'),
    path("project/add/", ProjectCreateView.as_view(), name='project_add'),
    path("project/<int:pk>", ProjectDetail.as_view(), name='project_detail'),
    path("project/<int:pk>/update/", ProjectUpdateView.as_view(), name='project_update'),
    path("project/<int:pk>/delete/", ProjectDeleteView.as_view(), name='project_delete'),
]
