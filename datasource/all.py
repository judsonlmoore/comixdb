# Documentation https://levelup.gitconnected.com/how-to-run-scrapy-spiders-in-your-program-7db56792c1f7
from scrapy.crawler import Crawler, CrawlerProcess
from scrapy.utils.project import get_project_settings

from datasource.spiders.explsom import ExplsomSpider

settings = get_project_settings()
process = CrawlerProcess(settings)

ExplsomSpider = Crawler(
    ExplsomSpider,
    settings={
        **settings,
        # "FEEDS": {
        #     "bikeberry.json": {"format": "json"},
        # },
    },
)
# chainreactioncycles_crawler = Crawler(
#     chainreactioncycles,
#     settings={
#         **settings,
#         # "FEEDS": {
#         #     "quotes.json": {"format": "json"},
#         # },
#     },
# )

process.crawl(ExplsomSpider)
# process.crawl(chainreactioncycles_crawler)

process.start()