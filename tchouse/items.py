# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class TchouseItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    region = scrapy.Field() 
    name = scrapy.Field()
    house_type = scrapy.Field() # 住宅／公寓
    room_type = scrapy.Field() 
    floor = scrapy.Field()		#楼层
    room_area = scrapy.Field()	#面积
    price = scrapy.Field()	
    publish_date = scrapy.Field()
    product_url = scrapy.Field()
    link_url = scrapy.Field()
    
    created_at = scrapy.Field()
    updated_at = scrapy.Field()
    pass
