import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from datasource.items import DatasourceItem
import hashlib
import time
from time import gmtime

class GoComicsSpider(CrawlSpider):
    name = 'gocomics'
    allowed_domains = ['gocomics.com']
    start_urls = ['https://www.gocomics.com/garfield/1992/02/19']
    rules = [
        Rule(LinkExtractor(
        allow='https://www.gocomics.com', deny=('/lists/','/collections/','/blog/')),
        callback='parse',
        follow=True
        )
    ]

    def parse(self, response):
        exists = response.xpath('//div[@data-shareable-model="FeatureItem"]')
        if exists:
            item = DatasourceItem()

            ## Universal fields
            item['id'] = hashlib.sha1(response.request.url.encode('utf-8')).hexdigest()
            item['sourceUrl'] = response.request.url

            ## Comic fields
            item['title'] = response.xpath('//meta[@property="og:title"]/@content').get().replace(' | GoComics.com', '')
            # item['authorName'] = response.xpath('//').get()
            # item['authorHandle'] = response.xpath('//a[contains(@class,"Author__Twitter")]/text()').get()
            # item['authorUrl'] = response.xpath('//a[contains(@class,"Author__Twitter")]/@href').get()
            # item['publishedDate'] = response.xpath('//').get()
            item['image_urls'] = response.xpath('//div[contains(@class,"comic__image")]//picture[@class="item-comic-image"]/img/@src').getall()

            ## Timestamp fields
            item['published_at'] = time.strftime("%B %d %Y", gmtime())
            item['updated_at'] = time.strftime("%B %d %Y", gmtime())

            yield item