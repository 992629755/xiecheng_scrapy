# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy import Item,Field


class XiechengItem(Item):
    collection = 'hainan'
    productID = Field()
    title = Field()
    price = Field()
    type = Field()
    grade = Field()