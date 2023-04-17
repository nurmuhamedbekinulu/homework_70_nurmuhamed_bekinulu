from django.db.models import Manager


class ProjectManager(Manager):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def get_or_none(self, pk=None):
        try:
            return self.get_queryset().get(pk=pk)
        except self.model.DoesNotExist:
            return None

    def get_deleted(self):
        return self.get_queryset().filter(is_deleted=True)

    def all(self):
        return self.get_queryset().filter(is_deleted=False)
