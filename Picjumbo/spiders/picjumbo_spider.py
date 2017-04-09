# -*- coding:utf-8 -*-

from scrapy.spiders import Spider
from scrapy.selector import Selector

from Picjumbo.items import PicjumboItem


class PicjumboSpider(Spider):
    name = "picjumbo_spider"

    allowed_domains = ['picjumbo.com']
    start_urls = [
        'https://picjumbo.com/'
    ]

    def parse(self, response):
        sel = Selector(response)
        urls = sel.xpath("//div[@class='tri_img_one']/img[@class='image']/@src").extract()       

        image_urls = []
        for target_url in urls:
            target_url = 'http:' + target_url[:-20]
            image_urls.append(target_url)

        item = PicjumboItem()
        item['image_urls'] = image_urls

        yield item