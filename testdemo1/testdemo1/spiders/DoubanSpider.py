
# -*- encoding:utf-8 -*-

from scrapy.spider import BaseSpider
from scrapy.http import Request
from scrapy.selector import HtmlXPathSelector
from testdemo1.items import TutorialItem

import re

class DoubanSpider(BaseSpider):
	name = "douban"
	allowed_domains = ["movie.douban.com"]
	start_urls = []

	def start_request(self):
		file_object = open("move_name.txt","r")

		try:
			url_head = "http://movie.douban.com/subject_search?search_text="
			for line in file_object.readlines:
				self.start_urls.append(url_head+line);

			for url in self.start_urls:
				yield self.make_requests_from_url(url)
		finally:
			file_object.close()

	def parse(self,response):

		hxs = HtmlXPathSelector(response)
		movie_link = hxs.select('//*[@id="content"]/div/div[1]/div[2]/table[1]/tr/td[1]/a/@href').extract()
		if movie_link:
			yield Request(movie_link[0],callable=self.parse_item)
		print "==========================="
		print response
		print "==========================="

	def parse_item(self,response):
		hxs = HtmlXPathSelector(response)
		move_name = hxs.select("//*[@id='content']/h1/span[1]/text()").extract()
		print move_name