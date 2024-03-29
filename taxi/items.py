# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

from scrapy.item import Item, Field


class TaxiServiceItem(Item):
    name = Field()
    fullname = Field()
    link = Field()
    location = Field()
    phones = Field()
