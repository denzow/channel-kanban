from django.db import models


class Kanban(models.Model):
    title = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return 'Kanban({}:{})'.format(self.id, self.title)

    @classmethod
    def get_by_id(cls, kanban_id):
        return cls.objects.get(pk=kanban_id)
