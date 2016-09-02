# -*- coding: utf-8 -*-

from __future__ import print_function

import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule

from phone_hunter.items import Phone


class SymphonySpider(CrawlSpider):
    name = 'symphony'
    allowed_domains = ['www.symphony-mobile.com']
    start_urls = [
        'https://www.symphony-mobile.com/product.php?cat=1&sub_cat=5'
    ]

    rules = (
        Rule(
            LinkExtractor(
                allow=r'/product-details.php\?id=\d+'
            ),
            callback='parse_product',
            follow=True),
        Rule(
            LinkExtractor(
                restrict_css=('ul.pagination li a',)
            ),
            follow=True),
    )

    def parse_product(self, response):
        item = Phone()
        item['model'] = response.css('h1.phonename::text').extract()
        if type(item['model']) == list:
            item['model'] = item['model'][0].strip()

        item['price'] = response.css('h4.pTag::text').extract()[0].strip()

        specs = response.xpath('//*[@id="spec"]/div/div[1]/div/table//tr')

        for spec in specs:
            feature, prop = spec.xpath('td/text()').extract()
            item["_".join(feature.lower().split())] = prop.strip()
        return item
