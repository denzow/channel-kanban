from django.db import models


class ChatLog(models.Model):

    room_name = models.CharField(max_length=100)
    message = models.TextField('message')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return 'ChatLog({}:{})'.format(self.room_name, self.message)
