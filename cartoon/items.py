# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class ComicItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    dir_name = scrapy.Field() #章节名
    link_url = scrapy.Field() #每一章节每一页的连接
    img_url = scrapy.Field() #图片链接
    img_paths = scrapy.Field() #图片保存路径
