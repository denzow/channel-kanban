# coding: utf-8
from django.contrib import admin
from .models import Kanban, Card, PipeLine

admin.site.register(Kanban)
admin.site.register(PipeLine)
admin.site.register(Card)
