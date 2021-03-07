URL = 'https://www.epicgames.com/store/ru/free-games'
from libs.items import EpicGame
from requests import get
import json
from datetime import datetime
import pytz
from libs.utils import needs_refresh

__RUS_TIME_FORMAT = "%d.%m.%Y %H:%M"
__DATE_FORMAT = "%Y-%m-%dT%H:%M:%S.%fZ"
__local_timezone = pytz.timezone("Europe/Moscow")


def query_epic_games(cached_games_infos: [EpicGame]):
    """
    This function queries Epic Games Store for current and coming soon games

    :return: list of EpicGame objects
    """
    if not needs_refresh([game.item_end_date_utc for game in cached_games_infos]):
        return cached_games_infos

    URL = 'https://store-site-backend-static.ak.epicgames.com/freeGamesPromotions?locale=ru&country=RU&allowCountries=RU'
    src = get(URL).content
    items = json.loads(src)['data']['Catalog']['searchStore']['elements']

    items = list((item for item in items if item['promotions']))

    promotionalItems = list(item for item in items if item['promotions']['promotionalOffers'])
    upcomingItems = list(item for item in items if item['promotions']['upcomingPromotionalOffers'])

    promotionalItems = sorted(promotionalItems, key=lambda x: datetime.strptime(
        x['promotions']['promotionalOffers'][0]['promotionalOffers'][0]['startDate'], __DATE_FORMAT))
    upcomingItems = sorted(upcomingItems, key=lambda x: datetime.strptime(
        x['promotions']['upcomingPromotionalOffers'][0]['promotionalOffers'][0]['startDate'], __DATE_FORMAT))

    epic_games = []
    for item in promotionalItems:
        item_price = item['price']['totalPrice']['fmtPrice']['originalPrice']
        item_name = item['title']
        item_img = item['keyImages'][0]['url']
        item_end_date = item['promotions']['promotionalOffers'][0]['promotionalOffers'][0]['endDate']
        item_end_date_utc = datetime.strptime(item_end_date, __DATE_FORMAT).replace(tzinfo=pytz.utc)
        item_end_date = item_end_date_utc.astimezone(__local_timezone).strftime(__RUS_TIME_FORMAT)

        item_message = f"Сейчас бесплатно до {item_end_date} (по Москве)"

        epic_game = EpicGame(item_price=item_price,
                             item_img=item_img,
                             item_status_message=item_message,
                             item_name=item_name,
                             item_end_date_utc=item_end_date_utc)
        epic_games.append(epic_game)

    for item in upcomingItems:
        item_price = item['price']['totalPrice']['fmtPrice']['originalPrice']
        item_name = item['title']
        item_img = EpicGame.NO_IMAGE_TAG
        item_start_date = item['promotions']['upcomingPromotionalOffers'][0]['promotionalOffers'][0]['startDate']
        item_end_date = item['promotions']['upcomingPromotionalOffers'][0]['promotionalOffers'][0]['endDate']
        item_end_date_utc = datetime.strptime(item_end_date, __DATE_FORMAT).replace(tzinfo=pytz.utc)
        item_start_date = datetime.strptime(item_start_date, __DATE_FORMAT).replace(tzinfo=pytz.utc).astimezone(
            __local_timezone).strftime(__RUS_TIME_FORMAT)

        item_message = f"Скоро появится, с {item_start_date} (по Москве)"

        epic_game = EpicGame(item_price=item_price,
                             item_img=item_img,
                             item_status_message=item_message,
                             item_name=item_name,
                             item_end_date_utc=item_end_date_utc)
        epic_games.append(epic_game)

    return epic_games
