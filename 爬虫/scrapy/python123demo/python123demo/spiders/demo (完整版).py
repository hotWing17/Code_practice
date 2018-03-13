# -*- coding: utf-8 -*-
import scrapy


class DemoSpider(scrapy.Spider):
    name = 'demo'

    def start_requests(self):
        urls = ['https://www.python123.io/ws/demo.html']
        #使用'yield'成为生成器函数，节省空间，一次只产生一个数值
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        fname = response.url.split('/')[-1]
        with open(fname, 'wb') as f:
            f.write(response.body)
        self.log('Saved file %s.' % name)
