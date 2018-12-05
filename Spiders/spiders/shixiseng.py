# -*- coding: utf-8 -*-
import scrapy


class ShixisengSpider(scrapy.Spider):
    name = 'shixiseng'
    allowed_domains = ['www.shixiseng.com']
    start_urls = ['https://www.shixiseng.com/']

    def parse(self, response):
        with open('test.html', 'w+') as f:
            f.write(response.text)
        pass
