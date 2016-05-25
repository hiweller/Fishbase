# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

# packages
import scrapy
class SalmoPicture(scrapy.Item):
	imName = scrapy.Field() # name of image, ex Sasal_u5
	fishSize = scrapy.Field() # in cm
	file_urls = scrapy.Field() # url of image
	files = scrapy.Field() # idk

class SalmoItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass
