# _*_ coding:utf-8 _*_
import scrapy
from grontho.items import GronthoItem
counter = 1
class bookCrawl(scrapy.Spider):
	name="grontho"
	allowed_domain = ["grontho.com"]
	start_urls = ["http://www.grontho.com/p?=1"]
	#start_urls = ["http://www.grontho.com/%E0%A6%86%E0%A6%AE%E0%A6%BF-%E0%A6%AC%E0%A7%80%E0%A6%B0%E0%A6%BE%E0%A6%99%E0%A7%8D%E0%A6%97%E0%A6%A8%E0%A6%BE-%E0%A6%AC%E0%A6%B2%E0%A6%9B%E0%A6%BF/"]

	def parse(self, response):
		global counter
		item = GronthoItem()
		item['bookNumber'] = counter
		item['pageLink'] = response.url
		tt = response.xpath('//div[@class="single_left"]//h1/text()').extract()
		item['bookTitle'] = tt[0]
		#item['bookTitle'] = repo

		for eachLink in response.xpath('//div[@class="single_left"]//p//a//@href').extract():
			if ".pdf" not in eachLink:
				item['bookLink'] = 'No PDF link is available'
			else:
				item['bookLink'] = eachLink
		#item.display['size'] = "6"
		#item.display['resolution'] = "6"
		counter += 1
		yield item

		NEXT_PAGE_SELECTOR = '.next_prev_cont .right a ::attr(href)'
		next_page = response.css(NEXT_PAGE_SELECTOR).extract_first()
		if next_page:
			yield scrapy.Request(response.urljoin(next_page),callback=self.parse)