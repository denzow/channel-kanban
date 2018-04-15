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


def update_kanban(pipeline_id, card_id_list):
    """
    パイプライン内のカードを更新する
    :return:
    """
    print('update_kanban')
    order = 0
    for card_id in card_id_list:
        card = Card.get_by_id(card_id=card_id)
        card.order = order
        card.pipeline_id = pipeline_id
        card.save()
        order += 1
        print(card)


