from django.db import models


class Card(models.Model):

    title = models.CharField(max_length=100)
    content = models.TextField()
    order = models.IntegerField()
    pipeline = models.ForeignKey('PipeLine', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return 'Card({}:{} belonged {}) '.format(self.id, self.title, self.pipeline)

    @property
    def json(self):
        return {
            'id': self.id,
            'title': self.title,
            'content': self.content,
        }

    @classmethod
    def create(cls, **params):
        return cls.objects.create(**params)

    @classmethod
    def get_by_id(cls, card_id):
        return cls.objects.get(pk=card_id)
