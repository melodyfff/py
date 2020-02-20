# -*- coding: utf-8 -*-
import scrapy

"""
ACG 次元漫画网列表爬取
"""


class OngAcgSpider(scrapy.Spider):
    name = 'ongacg'
    start_urls = ['https://bbs.ongacg.com/forum.php?mod=forumdisplay&fid=37&filter=typeid&typeid=4', ]

    def parse(self, response):
        print(response.xpath('.//tbody//tr//th//a[2]//text()').getall())
        for title in list(set(response.xpath('.//tbody//tr//th//a[2]//text()').getall())):
            yield {
                'title': title,
            }

        yield {
            'page': response.css('.pg strong::text').get(),
        }

        next_page = response.css('.nxt::attr("href")').get()
        if next_page is not None:
            yield response.follow(next_page, self.parse)
