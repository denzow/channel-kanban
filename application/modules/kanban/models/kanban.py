from django.db import models


class Kanban(models.Model):
    title = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return 'Kanban({}:{})'.format(self.id, self.title)

    @classmethod
    def get_by_id(cls, kanban_id):
        return cls.objects.get(pk=kanban_id)

    @classmethod
    def get_or_create(cls, kanban_id):
        try:
            return cls.get_by_id(kanban_id)
        except Exception:
            return Kanban.objects.create(
                title='new'
            )
