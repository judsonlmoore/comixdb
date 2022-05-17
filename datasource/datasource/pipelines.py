# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from scrapy.exceptions import DropItem
from itemadapter import ItemAdapter

class DuplicatesPipeline:
  def __init__(self):
    self.ids_seen = set()
  def process_item(self, item, spider):
    adapter = ItemAdapter(item)
    if adapter['id'] in self.ids_seen:
      raise DropItem(f"Duplicate item found: {item!r}")
    else:
      self.ids_seen.add(adapter['id'])
    return item

class EmptyPipeline(object):
  def process_item(self, item, spider):
    if item['image_urls']:
      # print item['image_urls']
      return item
    else:
      raise DropItem("Empty entry")

class MinTextPipeline(object):
    def __init__(self):
        self.minimum = 5

    def process_item(self, item, spider):
      if item['authorName']:
        if len(item['authorName']) < self.minimum:
          item['authorName'] = item['authorName'][0:self.minimum]
        return item
      else:
        return DropItem('Missing authorName')

    def process_item(self, item, spider):
      if item['authorHandle']:
        if len(item['authorHandle']) < self.minimum:
          item['authorHandle'] = item['authorHandle'][0:self.minimum]
        return item
      else:
        return DropItem('Missing authorHandle')