# -*- coding: utf-8   -*-

# Define here the models for your scraped items
# product, price
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

from scrapy.item import Item, Field 


class WebbotItem(Item):
    # Define the fields for your item here like:
    # Name = scrapy.Field()
    product = Field()
    price = Field() 
