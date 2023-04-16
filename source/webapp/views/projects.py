from webapp.models import Project, Task
from webapp.forms import ProjectForm
from django.views.generic import DeleteView, CreateView, UpdateView, ListView
from django.urls import reverse, reverse_lazy
from webapp.forms import SearchForm
from django.db.models import Q
from django.utils.http import urlencode


class ProjectCreateView(CreateView):
    template_name = 'projects/project_create.html'
    model = Project
    form_class = ProjectForm

    def get_success_url(self):
        return reverse('project_detail', kwargs={'pk': self.object.pk})


class ProjectDetail(DeleteView):
    template_name = 'projects/project.html'
    model = Project


class ProjectUpdateView(UpdateView):
    template_name = 'projects/project_update.html'
    form_class = ProjectForm
    model = Project

    def get_success_url(self):
        return reverse('project_detail', kwargs={'pk': self.object.pk})


class ProjectDeleteView(DeleteView):
    template_name = 'projects/project_confirm_delete.html'
    model = Project
    success_url = reverse_lazy('project_index')


class ProjectIndexView(ListView):
    template_name = 'projects/index.html'
    model = Project
    context_object_name = "projects"
    paginate_by = 10
    paginate_orphans = 1

    def get(self, request, *args, **kwargs):
        self.form = self.get_search_form()
        self.search_value = self.get_search_value()
        return super().get(request, *args, **kwargs)

    def get_search_form(self):
        return SearchForm(self.request.GET)

    def get_search_value(self):
        if self.form.is_valid():
            return self.form.cleaned_data['search']
        return None

    def get_queryset(self):
        queryset = super().get_queryset().exclude(is_deleted=True)
        if self.search_value:
            query = Q(title__icontains=self.search_value) | Q(
                description__icontains=self.search_value)
            queryset = queryset.filter(query)
        return queryset

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(object_list=object_list, **kwargs)
        context['form'] = self.form
        if self.search_value:
            context['query'] = urlencode({'search': self.search_value})
        return context
