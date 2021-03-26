# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import json
from scrapy.exceptions import DropItem
from scrapy.exporters import JsonLinesItemExporter
from unidecode import unidecode
import pymongo


class BirdiechalengePipeline:
    name_col = "ofertas"

    def __init__(self,mongo_uri,mongo_db):
        self.mongo_uri = mongo_uri
        self.mongo_db = mongo_db

    def open_spider(self,spider):
        self.client = pymongo.MongoClient(self.mongo_uri)
        self.db = self.client[self.mongo_db]
        self.client.drop_database(self.db)
        self.col = self.db[self.name_col]


    @classmethod
    def from_crawler(cls, crawler):
        return cls(
            mongo_uri=crawler.settings.get('MONGO_URI'),
            mongo_db=crawler.settings.get('MONGO_DATABASE','dados')
        )

    def process_item(self, item, spider):
        adapter = ItemAdapter(item)
        if 'name' in adapter.keys() and 'price' in adapter.keys():
            adapter['name'] = [unidecode(adapter['name'][0])]
            adapter['price'] = [unidecode(adapter['price'][0])]
            str_price = adapter['price'][0]
            str_price = str_price.replace('.','')
            str_price = str_price.replace(',','.')
            price = float(str_price)
            if 'cents' in adapter.keys():
                cents = adapter['cents'][0]
                cents = float(cents)
                price = price + cents/100
            adapter['price'] = price
            self.col.insert_one(adapter.asdict())
            print("Exporter:",adapter["name"],"| ",adapter["price"], "|",adapter['store'])

        else:
           raise DropItem(f"{item} without name or price")
        
        return item


