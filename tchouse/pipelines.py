# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

import codecs
import json

class TchousePipeline(object):
    def process_item(self, item, spider):
        return item

class JsonWriterPipeline(object):

    def __init__(self):
        self.file = codecs.open('house.json', 'wb', encoding='utf-8')

    def process_item(self, item, spider):
        line = json.dumps(dict(item), ensure_ascii=False) + "\n"
        self.file.write(line)
        return item

    def spider_closed(self, spider):
        self.file.close()

        file = codecs.open(filename, 'wb', encoding='utf-8')