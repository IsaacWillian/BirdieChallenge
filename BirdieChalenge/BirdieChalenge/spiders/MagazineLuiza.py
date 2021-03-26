import scrapy
from scrapy.loader import ItemLoader
from BirdieChalenge.items import BirdiechalengeItem
from datetime import datetime
import json
from scrapy_splash import SplashRequest


class MagazineluizaSpider(scrapy.Spider):
    name = 'MagazineLuiza'
    start_urls = json.load(open("../urlsBuffers/magazineluiza"))

    def start_request(self):
        for url in self.start_urls:
            yield Request(url, headers=headers)

    def parse(self, response):
        l = ItemLoader(BirdiechalengeItem(), response)
        l.add_xpath('name', '//h1[@class="header-product__title"]/text()')
        l.add_xpath('price', '//span[@class="price-template__text"]/text()')
        l.add_value('store', "Magazine Luiza")
        l.add_value('url', response.url)
        l.add_value('last_update', datetime.today())
        yield l.load_item()