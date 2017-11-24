# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class HexunItem(scrapy.Item):
    name = scrapy.Field()
#建立url存储文章url网址
    url= scrapy.Field()
#建立hits存储文章阅读数
    hits= scrapy.Field()
#建立comment存储文章评论数
    comment= scrapy.Field()
