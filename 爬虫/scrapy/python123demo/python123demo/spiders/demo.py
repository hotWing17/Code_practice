# -*- coding: utf-8 -*-
import scrapy


class DemoSpider(scrapy.Spider):
    name = 'demo'
    #allowed_domains = ['python123.io']
    # 修改程需要爬取的这个链接
    # 表示爬虫启动时开始的链接
    start_urls = ['https://www.python123.io/ws/demo.html']

    # parse()用于处理响应，解析内容形成字典，发现新的url爬取请求
    # 参数(self:是面向对象所属关系的标记;response:从网站返回内容存储的对应的对象)
    def parse(self, response):
        fname = response.url.split('/')[-1]
        with open(fname, 'wb') as f:
            f.write(response.body)
        self.log('Saved file %s.' % name)
        pass
