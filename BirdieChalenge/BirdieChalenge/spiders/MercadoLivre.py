import scrapy
from scrapy.loader import ItemLoader
from BirdieChalenge.items import BirdiechalengeItem
from datetime import datetime
import json
from scrapy_splash import SplashRequest


class MercadolivreSpider(scrapy.Spider):
    name = 'MercadoLivre'
    start_urls = json.load(open("../urlsBuffers/mercadolivre"))
   
    def start_request(self):
        for url in self.start_urls:
            yield Request(url, headers=headers)

    def parse(self, response):
        l = ItemLoader(BirdiechalengeItem(), response)
        l.add_xpath('name', '//h1[@class="ui-pdp-title"]/text()')
        l.add_xpath('price', '//div[@class="ui-pdp-price__second-line"]/span[@class="price-tag ui-pdp-price__part"]/span[@class="price-tag-fraction"]/text()')
        l.add_xpath('cents', '//div[@class="ui-pdp-price__second-line"]/span[@class="price-tag ui-pdp-price__part"]/span[@class="price-tag-cents"]/text()')
        l.add_value('store', "Mercado Livre")
        l.add_value('url', response.url)
        l.add_value('last_update', datetime.today())
        yield l.load_item()
