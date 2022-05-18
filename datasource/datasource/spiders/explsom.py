from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from datasource.items import DatasourceItem
import hashlib
import time
from time import gmtime

class ExplsomSpider(CrawlSpider):
    name = 'explsom'
    allowed_domains = ['explosm.net']
    start_urls = ['https://explosm.net/comics/hourglass-figure']
    rules = [
        Rule(LinkExtractor(
        allow='http://explosm.net/comics/'),
        callback='parse',
        follow=True
        )
    ]

    def parse_item(self, response):
        exists = response.xpath('//div[@id="comic"]')
        if exists:
            item = DatasourceItem()

            ## Universal fields
            item['id'] = hashlib.sha1(response.request.url.encode('utf-8')).hexdigest()
            item['sourceUrl'] = response.request.url

            ## Comic fields
            # item['title'] = response.xpath('//').get()
            # item['authorName'] = response.xpath('//').get()
            item['authorHandle'] = response.xpath('//a[contains(@class,"Author__Twitter")]/text()').get()
            item['authorUrl'] = response.xpath('//a[contains(@class,"Author__Twitter")]/@href').get()
            # item['publishedDate'] = response.xpath('//').get()
            # item['image_urls'] = response.xpath('//div[contains(@class,"MainComic")]/span/img/@src').getall()

            ## Timestamp fields
            item['published_at'] = time.strftime("%B %d %Y", gmtime())
            item['updated_at'] = time.strftime("%B %d %Y", gmtime())

            yield item