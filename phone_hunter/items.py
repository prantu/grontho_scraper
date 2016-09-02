# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class Phone(scrapy.Item):
    model = scrapy.Field()
    os = scrapy.Field()
    display = scrapy.Field()
    camera = scrapy.Field()

    processor = scrapy.Field()
    processor_core = scrapy.Field()
    processor_64bit = scrapy.Field()

    ram = scrapy.Field()
    rom = scrapy.Field()

    expandable_memory = scrapy.Field()
    sim = scrapy.Field()
    battery = scrapy.Field()
    multimedia = scrapy.Field()
    dimension = scrapy.Field()
    connectivity = scrapy.Field()

    price = scrapy.Field()
