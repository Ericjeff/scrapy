
# -*- encoding:utf-8 -*-

import scrapy
from testdemo1.items import Testdemo1Item


'''
	xpath(): 传入xpath表达式，返回该表达式所对应的所有节点的selector list列表 。
	css(): 传入CSS表达式，返回该表达式所对应的所有节点的selector list列表.
	extract(): 序列化该节点为unicode字符串并返回list。
	re(): 根据传入的正则表达式对数据进行提取，返回unicode字符串list列表。
	div[@class="mine"]
'''

class csdn(scrapy.Spider):

	name = "csdn"
	start_urls = [
			"http://blog.csdn.net/zq602316498/article/details/61622666"
	]

	def parse(self,response):
		print "=================================="
		print  response.headers
		print "=================================="

		item = Testdemo1Item()
		art =  response.xpath("//article")
		item['title'] = art.xpath("//h1/text()").extract()
		item['readNum'] = art.xpath("//button[@class='btn-noborder']/span/text()").extract()
		item['content'] = art.xpath("//div[@id='article_content']/div").extract()

		print "=================================="
		print item['title']
		print "=================================="
		print item['readNum']
		print "=================================="
		print item['content']
		print "=================================="
		yield item
'''
    art.xpath("//button[@class='btn-noborder'"]/span/text()).extract()
	art.xpath("//div[@id='article_content']/div").extract()
	art.xpath("//h1/text()").extract()
	raise KeyError("Spider not found: {}".format(spider_name))
KeyError: 'Spider not found: fuckSpider'

	Could not find a version that stisfies the requirement pywin32(from versions:)
	No matching distrivution found for pywin32

	python version 2.7 required,which was not found in the registry
'''