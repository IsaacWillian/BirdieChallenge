## Spider parado 
## Dificuldade em extrair dados do JS
## Nome aparece no Js porém o preço não aparece
## função js2xml.parse retorna erros

import scrapy
from scrapy.loader import ItemLoader
from BirdieChalenge.items import BirdiechalengeItem
import pandas as pd
from datetime import date
import json
import js2xml


class CasasbahiaSpider(scrapy.Spider):
    name = 'CasasBahia'
    start_urls = json.load(open("../urlsBuffers/casasbahia"))
    
    def start_request(self):
        for url in self.start_urls:
            yield Request(url, headers=headers) 

    def parse(self, response):
        script = response.xpath('//script[@id="__NEXT_DATA__"]/text()').get()
        print(script)
        script_as_xml = js2xml.parse(script)
        print(script_as_xml)
        sel = scrapy.Selector(_root=script_as_xml)
        l = ItemLoader(BirdiechalengeItem(), response)
        l.add_xpath('name', '//h1[@class=" css-1pnb2jm eym5xli0"]/text()')
        l.add_xpath('price', '//span[@class="product-price-value"]/text()')
        l.add_value('store', "Casas Bahia")
        l.add_value('url', response.url)
        l.add_value('last_update', date.today())

        yield l.load_item()