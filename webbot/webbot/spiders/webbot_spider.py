# -*- coding: utf-8 -*-

from scrapy.spider import Spider 
from scrapy.selector import Selector
from amazon.items import AmazonItem

class AmazonSpider(Spider):
    name = "amazon"
    allowed_domains = ["amazon.co.jp"]
    start_urls = [
        "http://www.amazon.co.jp/s/ref=sr_in_-2_p_89_36?rh=n%3A160384011%2Cn%3A%21161669011%2Cn%3A170303011%2Cn%3A170329011%2Cp_89%3A花王%28Kao%29&bbn=170329011&ie=UTF8&qid=1415441255&rnid=2321255051"
    ]

    def parse(self, response):
        filename = 'cao.html' 
        with open(filename, 'wb') as f:
            f.write(response.body)
        sel = Selector(response)
        mechans = sel.xpath('//a/span[@class="bld lrg red"]/text()')
        items = []
        for mechan in mechans:
            item = AmazonItem()
            item['price'] = mechan.extract() 
            items.append(item)
        return items