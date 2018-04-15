# coding: utf-8

from .models import Kanban, PipeLine, Card


def get_whole_json(kanban_id):
    kanban = Kanban.get_by_id(kanban_id)
    pipeline_list = PipeLine.get_list_by_kanban_id(kanban.id)
    result = []
    for pipeline in pipeline_list:
        result.append({
            'id': pipeline.id,
            'title': pipeline.title,
            'cards': [card.json for card in pipeline.cards]
        })

    return result
