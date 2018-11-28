# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import re

import pymongo

from .items import XiechengItem


class MongoPipeline(object):
    def __init__(self, mongo_uri, mong_db):
        self.mongo_uri = mongo_uri
        self.mongo_db = mong_db


    @classmethod
    def from_crawler(cls,crawler):
        return cls(mongo_uri=crawler.settings.get('MONGO_URI'),mong_db=crawler.settings.get('MONGO_DB'))

    def open_spider(self, spider):
        self.client = pymongo.MongoClient(self.mongo_uri)
        self.db = self.client[self.mongo_db]

    def process_item(self, item, spider):
        if item['productID']:
            rs = re.match('^{"Id":\s(\d+),"', item['productID']).group(1)
            item['productID'] = int(rs)
            item['price'] = int(item['price'])
            item['grade'] = int(item['grade'])

            self.db[XiechengItem.collection].insert(dict(item))
        return item

    def close_spider(self, spider):
        self.client.close()


