URL = 'https://www.epicgames.com/store/ru/free-games'
from libs.items import EpicGame
from requests import get
import json

def query_epic_games():
    """
    This function queries Epic Games Store for current and coming soon games

    :return: list of EpicGame objects
    """
    URL = 'https://store-site-backend-static.ak.epicgames.com/freeGamesPromotions?locale=ru&country=RU&allowCountries=RU'
    src = get(URL).content
    items = json.loads(src)['data']['Catalog']['searchStore']['elements']

    epic_games = []

    for item in items[:2]:
        item_price = item['price']['totalPrice']['fmtPrice']['originalPrice']
        item_name = item['title']
        if (len(epic_games) > 0 ):
            item_img = EpicGame.NO_IMAGE_TAG
            item_message = "Скоро появится"
            effective_date = item['effectiveDate'][0:10]
            epic_games[0].item_status_message = f"Сейчас бесплатно (до {effective_date})"
        else:
            item_img = item['keyImages'][0]['url']
            item_message = "Сейчас бесплатно"

        epic_game = EpicGame(item_price=item_price,
                             item_img=item_img,
                             item_status_message=item_message,
                             item_name=item_name)
        epic_games.append(epic_game)

    return epic_games
