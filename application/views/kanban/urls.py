from django.urls import path

from . import views

urlpatterns = [
    path('<int:kanban_id>', views.index, name='index'),
]


