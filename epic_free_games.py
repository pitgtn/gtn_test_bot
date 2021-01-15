from selenium import webdriver  # $ pip install selenium
import lxml.html as LH
from bs4 import BeautifulSoup
def epic():
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')
# get chromedriver from
# https://sites.google.com/a/chromium.org/chromedriver/downloads
    browser = webdriver.Chrome(chrome_options=options)
    host = 'https://www.epicgames.com'
    browser.get('https://www.epicgames.com/store/ru/free-games')
# ... other actions
    src = browser.page_source
    browser.close()
    browser.quit()


    soup = BeautifulSoup(src, 'lxml')
    items = soup.find_all('div', {"data-component":"WithClickTrackingComponent"})
    new_epic_game = ''
    for i in items:
        item_link = i.find('a').get('href')
        item_img = i.find('img').get('data-image')
        item_message = i.find('span', {"data-component":"Message"}).text
        item_name = i.find('span', {"data-component": "OfferTitleInfo"}).text
        s = (f"<a href=\"{item_img}\">&#8203;</a>\n{item_message} - <a href=\"{host}{item_link}\"><b>{item_name}</b></a>\n")
        new_epic_game += s
    return new_epic_game
