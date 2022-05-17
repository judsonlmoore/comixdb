# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy

class DatasourceItem(scrapy.Item):

    ## Universal fields
    id = scrapy.Field()
    sourceUrl = scrapy.Field()

    ## Comic fields
    title = scrapy.Field()
    authorName = scrapy.Field()
    authorHandle = scrapy.Field()
    authorUrl = scrapy.Field()
    publishedDate = scrapy.Field()
    image_urls = scrapy.Field()

    ## Timestamp fields
    published_at = scrapy.Field()
    updated_at = scrapy.Field()

    pass
