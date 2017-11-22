import datetime
import os

import requests
import trello
import vk
from vk.photos import Photo

import config


def is_image_file(attachment_url):
    _, file_extension = os.path.splitext(attachment_url)

    if file_extension not in ('.jpg', '.gif', '.png'):
        return False

    return True


def download_attachment(attachment_url):
    response = requests.get(attachment_url, stream=True)
    return response.content


def get_attachment_in_card(card):
    attachment_items = (attachment for attachment in card.get_attachments() if is_image_file(attachment.url))

    for attachment in attachment_items:
        binary_content = download_attachment(attachment.url)
        _, filename = os.path.split(attachment.url)
        yield (filename, binary_content)


def is_card_can_published(trello_card):
    if not trello_card.due_date:
        return False

    now_unixtime = datetime.datetime.utcnow().replace(tzinfo=None).timestamp()
    card_due_unixtime = trello_card.due_date.replace(tzinfo=None).timestamp()

    delta = card_due_unixtime - now_unixtime
    return True if delta <= 0 else False


if __name__ == '__main__':
    vk.set_access_token(config.VK_ACCESS_TOKEN)
    group = vk.get_group(config.VK_GROUP)

    client = trello.TrelloClient(api_key=config.TRELLO_KEY, token=config.TRELLO_TOKEN)

    board = client.get_board(config.TRELLO_BOARD)

    card_items = (card for card in board.open_cards() if is_card_can_published(card))

    for card in card_items:
        attachment_items = \
            {filename: binary_content for filename, binary_content in get_attachment_in_card(card)}
        photo_items = Photo.upload_wall_photos_for_group(group.id, attachment_items.items())
        group.wall_post(message=card.name + '\n' + card.description, attachments=photo_items)
        card.set_due_complete()
