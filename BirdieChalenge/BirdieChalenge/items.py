# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

from scrapy.item import Item, Field


class BirdiechalengeItem(Item):
    name = Field()
    price = Field()
    cents = Field()
    store = Field()
    url = Field()
    last_update = Field()

