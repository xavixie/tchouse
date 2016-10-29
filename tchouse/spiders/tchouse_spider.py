#tchouse_spider.py

import scrapy
import datetime

class TCHouseSpider(scrapy.Spider):
    name = "tchouse"

    def start_requests(self):
        urls = [
            'http://www.housetc.com/sell/'
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        for sel in response.css(".overflow table tbody tr"):
            # item = TchouseItem()
            # item['name'] = sel.css(".th-title .s1 a::text").extract_first()
            # print(item['name'])
            yield {

            	'region': sel.css(':first-child::text').extract_first(),
                'name': sel.css('.th-title .s1 a::text').extract_first(),
                'link_url': sel.css('.th-title .s1 a::attr(href)').extract_first(),
                'house_type': sel.css('td:nth-child(3)::text').extract_first(),
                'room_type': sel.css('td:nth-child(4)::text').extract_first(),
                'floor': sel.css('td:nth-child(5)::text').extract_first(),
                'room_area': sel.css('td:nth-child(6)::text').extract_first(),
                'price': sel.css('td:nth-child(7)::text').extract_first(),
                'publish_date': sel.css('td:nth-child(8)::text').extract_first(),

                'product_url' : response.url,
            }

        # Following links

        # next_page = response.css('.page :last-child::attr(href)').extract_first()
        # if next_page is not None:
        #     next_page = response.urljoin(next_page)
        #     yield scrapy.Request(next_page, callback=self.parse)