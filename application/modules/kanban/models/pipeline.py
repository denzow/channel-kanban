from django.db import models


class PipeLine(models.Model):

    kanban = models.ForeignKey('Kanban', on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    order = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return 'PipeLine({}:{} belonged {}) '.format(self.id, self.title, self.kanban)

    @property
    def cards(self):
        cards = self.card_set.order_by('order')
        return cards

    @property
    def json(self):
        return {
            'id': self.id,
            'title': self.title,
        }

    @classmethod
    def create(cls, **params):
        return cls.objects.create(**params)

    @classmethod
    def get_list_by_kanban_id(cls, kanban_id):
        return cls.objects.filter(kanban_id=kanban_id).order_by('order')
