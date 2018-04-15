# chat/views.py
from django.shortcuts import render
from django.utils.safestring import mark_safe
import json


def index(request, kanban_id):
    return render(request, 'kanban/index.html', {
        'kanban_id': kanban_id
    })
