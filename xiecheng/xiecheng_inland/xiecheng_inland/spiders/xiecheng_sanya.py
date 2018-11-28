# -*- coding: utf-8 -*-
from urllib.parse import quote

import scrapy
from scrapy import Request

from xiecheng_inland.items import XiechengItem
import re as RE

class XiechengSanyaSpider(scrapy.Spider):
    name = 'xiecheng_sanya'
    allowed_domains = ['http://vacations.ctrip.com/']
    start_urls = ['http://vacations.ctrip.com/tours/d-hainan-100001/p']

    def start_requests(self):
        # for keyword in self.settings.get('KEYWORDS'):
        for page in range(1,self.settings.get('MAX_PAGE')+1):
                # url = self.start_urls[0]+keyword+'-100001'
            url = self.start_urls[0] + str(page)
            yield Request(url=url, callback=self.parse, meta={'page':page}, dont_filter=True)

    def parse(self, response):
        products = response.xpath('//div[@id="_prd"]/div')
        for product in products:
            item = XiechengItem()
            item['productID']=''.join(product.xpath('./@data-params').extract())
            item['title'] = ''.join(product.xpath(".//h2/a/text()[1]").extract())
            item['price'] = ''.join(product.xpath(".//span[@class='sr_price']/strong/text()").extract())
            item['type'] = ''.join(product.xpath("./div[@class='product_pic']/em/text()").extract())
            item['grade'] = ''.join(product.xpath(".//p/strong/text()").extract())

            yield item



