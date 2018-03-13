# -*- coding: utf-8 -*-
import scrapy
import re


class StocksSpider(scrapy.Spider):
    name = 'stocks'
    start_urls = ['http://quote.eastmoney.com/stocklist.html']

    # parse()为页面处理函数
    def parse(self, response):
        # Scrapy爬虫支持多种HTML信息提取方法(查找<a>标签的‘href’属性的值)
        for href in response.css('a::attr(href)').extracts():
            try:
				stock = re.findall(r'[s][hz]\d{6}', href)[0]
				url   = 'https://gupiao.baidu.com/stock/' + stock + '.html'
                # 因为'yield'关键词，使parse()函数变成一个生成器
                # 下面函数参数(callback:给出了处理这个url对应响应的处理函数)
                yield scrapy.Request(url, callback=self.parse_stock)
            except:
                continue

    def parse_stock(self, response):
        # 本函数最终要返回提取的信息给Item Pipeline，应该是一个字典类型
        infoDict = {}
        # 使用<html>.css.('a::attr(href)').extracts()函数来提取信息
        # 为了提取真实的原文数据，需要调用 .extract() 方法如下
		stockInfo = response.css('.stock-bets')
		name      = stockInfo.css('.bets-name').extracts()[0]
		keyList   = stockInfo.css('dt').extracts()
		valueList = stockInfo.css('dd').extracts()
        for i in range(len(keyList)):
            key = re.findall(r'>.*</dt>', keyList[i])[0][1:-5]
            try:
                val = re.findall(r'\d+\.?.*</dd>', valueList[i])[0][1:-5]
            except:
                val = '--'
            infoDict[key] = val

        infoDict.update(
            {'股票名称': re.findall('\s.*\(', name)[0].split()[0] +
             re.findall('\>.*\<', name)[0][i:-1]})
        yield infoDict
